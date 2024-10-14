from django.shortcuts import render
from django.urls import reverse
from typing import Any

# Create your views here.

from . models import * 
from . forms import *
from django.views.generic import ListView, DetailView, CreateView

# class-based view
class ShowAllView(ListView):
    '''A view to show all Profiles.'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'


class ShowProfilePageView(DetailView):

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = "profile"

class CreateProfileView(CreateView):

    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    #def get_absolute_url(self) -> str:
        #'''return the URL to redirect to after sucessful create'''
 
        #return reverse("profile_page", kwargs={'pk': self.object.pk})
    
class CreateStatusMessageView(CreateView):

    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    # what to do after form submission?
    def get_success_url(self) -> str:
        '''return the URL to redirect to after sucessful create'''
        #return "/blog/show_all"
        #return reverse("show_all")
        return reverse("profile_page", kwargs=self.kwargs)
    
    def form_valid(self, form):
        '''this method executes after form submission'''

        print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        # find the article with the PK from the URL
        # self.kwargs['pk'] is finding the article PK from the URL
        profile_page = Profile.objects.get(pk=self.kwargs['pk'])

        # attach the article to the new Comment 
        # (form.instance is the new Comment object)
        form.instance.profile = profile_page

        # delegaute work to the superclass version of this method
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''
        build the template context data --
        a dict of key-value pairs.'''

        # get the super class version of context data
        context = super().get_context_data(**kwargs)

        # find the article with the PK from the URL
        # self.kwargs['pk'] is finding the article PK from the URL
        profile_page = Profile.objects.get(pk=self.kwargs['pk'])

        # add the article to the context data
        context['profile_page'] = profile_page

        return context
    