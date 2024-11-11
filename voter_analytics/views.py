from datetime import date
from django.shortcuts import render
from . models import * 
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView
from django.db.models.query import QuerySet
from django.db.models.functions import Substr
from django.db.models import Count
import plotly
import plotly.graph_objects as go



class AllVotersView(ListView):

    model = Voter
    template_name = 'voter_analytics/all_voters.html'
    context_object_name = 'voters'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['zip_code'] = Voter.objects.values_list('zip_code', flat=True).distinct()
        context['party'] = Voter.objects.values_list('party', flat=True).distinct()
        current_year = date.today().year
        context['years'] = range(1900, current_year + 1)
        return context

    def get_queryset(self) -> QuerySet[Any]:
        '''return the set of Results'''

        # use the superclass version of the queryset
        qs = super().get_queryset()


        # if we have a search paramter, use it to filter the query set
        if 'zip_code' in self.request.GET:
            zip_code = self.request.GET['zip_code']
            if zip_code: # not empty string:
                qs = qs.filter(zip_code__icontains=zip_code)
            
        if 'party' in self.request.GET:
            party = self.request.GET['party']
            if party: # not empty string:
                qs = qs.filter(party__icontains=party)

        if 'min_birth_year' in self.request.GET:
            min_birth_year = self.request.GET.get('min_birth_year')
            if min_birth_year:
                qs = qs.annotate(birth_year=Substr('birthday', 1, 4)).filter(birth_year__gte=min_birth_year)

        if 'max_birth_year' in self.request.GET:
            max_birth_year = self.request.GET.get('max_birth_year')
            if max_birth_year:
                qs = qs.annotate(birth_year=Substr('birthday', 1, 4)).filter(birth_year__lte=max_birth_year)


        return qs

class DetailVoterView(DetailView):
    model = Voter
    template_name = 'voter_analytics/detail_voter.html'
    context_object_name = 'voter'

class GraphView(ListView):
    model = Voter
    template_name = 'voter_analytics/graphs.html'
    context_object_name = 'voters_graph'

    def get_queryset(self):
        qs = super().get_queryset()
        
        # retrieve filter values from the request
        party = self.request.GET.get('party')
        min_birth_year = self.request.GET.get('min_birth_year')
        max_birth_year = self.request.GET.get('max_birth_year')
        voter_score = self.request.GET.get('voter_score')
        elections = ['v20_state', 'v21_town', 'v21_primary', 'v22_general', 'v23_town']

        # apply filters based on query parameters
        if party:
            qs = qs.filter(party=party)
        if min_birth_year:
            qs = qs.annotate(birth_year=Substr('birthday', 1, 4)).filter(birth_year__gte=min_birth_year)
        if max_birth_year:
            qs = qs.annotate(birth_year=Substr('birthday', 1, 4)).filter(birth_year__lte=max_birth_year)
        if voter_score:
            qs = qs.filter(voter_score=voter_score)
        for election in elections:
            if self.request.GET.get(election):
                qs = qs.filter(**{f"{election}__iexact": "TRUE"})

        return qs

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        current_year = date.today().year
        context['years'] = range(1900, current_year + 1)
        context['party'] = Voter.objects.values_list('party', flat=True).distinct()
        context['voter_scores'] = Voter.objects.values_list('voter_score', flat=True).distinct()
        context['election_fields'] = ['v20_state', 'v21_town', 'v21_primary', 'v22_general', 'v23_town']


        voters = self.get_queryset().annotate(birth_year=Substr('birthday', 1, 4))
        birth_year_data = voters.values('birth_year').annotate(count=Count('id')).order_by('birth_year')

        # prepare data for the bar chart
        x = [year_data['birth_year'] for year_data in birth_year_data]
        y = [year_data['count'] for year_data in birth_year_data]

        # create the bar chart
        fig = go.Bar(x=x, y=y)
        graph_div = plotly.offline.plot({"data": [fig]},
                                        auto_open=False,
                                        output_type="div")

        # add the graph to the context
        context['graph_div'] = graph_div

        party_data = self.get_queryset().values('party').annotate(count=Count('id')).order_by('party')

        # prepare data for the pie chart
        labels = [item['party'] for item in party_data]
        values = [item['count'] for item in party_data]

        # create the pie chart
        pie_trace = go.Pie(labels=labels, values=values)
        pie_div = plotly.offline.plot({"data": [pie_trace]},
                                    auto_open=False,
                                    output_type="div")

        # add the pie chart to the context
        context['pie_div'] = pie_div

        election_fields = ['v20_state', 'v21_town', 'v21_primary', 'v22_general', 'v23_town']
        election_labels = {
            'v20_state': '2020 State Election',
            'v21_town': '2021 Town Election',
            'v21_primary': '2021 Primary Election',
            'v22_general': '2022 General Election',
            'v23_town': '2023 Town Election',
        }

        # count voters who participated in each election
        participation_counts = [
            {
                'election': election_labels[field],
                'count': self.get_queryset().filter(**{f"{field}__iexact": "TRUE"}).count()
            }
            for field in election_fields
        ]

        # prepare data for the bar chart
        x = [item['election'] for item in participation_counts]
        y = [item['count'] for item in participation_counts]

        # create the bar chart
        fig = go.Bar(x=x, y=y)
        participation_div = plotly.offline.plot({"data": [fig]},
                                                auto_open=False,
                                                output_type="div")

        # add the participation chart to the context
        context['participation_div'] = participation_div

        return context