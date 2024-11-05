from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from typing import Any

# Create your views here.

from . models import * 
from . forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login


# class-based view
class ShowAllView(ListView):
    '''A view to show all Profiles.'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['profile'] = get_object_or_404(Profile, user=self.request.user)
        return context


class ShowProfilePageView(DetailView):

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = "profile"

class CreateProfileView(CreateView):

    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"

    def get_login_url(self) -> str:
        '''return the URL required for login'''
        return reverse('login') 
    
    def get_context_data(self, **kwargs: Any) -> dict:
        context = super().get_context_data(**kwargs)
        context['user_creation_form'] = UserCreationForm()
        return context

    def form_valid(self, form):
        ''' Reconstruct the UserCreationForm from submitted POST data'''
        user_creation_form = UserCreationForm(self.request.POST)

        if user_creation_form.is_valid():

            user = user_creation_form.save()

            login(self.request, user)

            form.instance.user = user

            return super().form_valid(form)
        else:
            return self.form_invalid(form)

    
class CreateStatusMessageView(LoginRequiredMixin, CreateView):

    form_class = CreateStatusMessageForm
    template_name = "mini_fb/create_status_form.html"

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
    
    # what to do after form submission?
    def get_success_url(self):
        profile = get_object_or_404(Profile, user=self.request.user)
        return reverse("profile_page", kwargs={"pk": profile.pk})
    
    def form_valid(self, form):
        '''this method executes after form submission'''

        print(f'CreateStatusMessageView.form_valid(): form={form.cleaned_data}')
        print(f'CreateStatusMessageView.form_valid(): self.kwargs={self.kwargs}')

        # find the article with the PK from the URL
        # self.kwargs['pk'] is finding the article PK from the URL
        profile_page = get_object_or_404(Profile, user=self.request.user)

        # attach the article to the new Comment 
        # (form.instance is the new Comment object)
        form.instance.profile = profile_page

        sm = form.save()

        files = self.request.FILES.getlist('files')
        
        for file in files:
            image = Image()  
            image.image_file = file  
            image.status_message = sm  
            image.save()  
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
        profile_page = get_object_or_404(Profile, user=self.request.user)

        # add the article to the context data
        context['profile_page'] = profile_page

        return context
    
class UpdateProfileView(LoginRequiredMixin, UpdateView):

    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"

    def form_valid(self, form):
        '''
        Handle the form submission to create a new Article object.
        '''
        print(f'UpdateProfileView: form.cleaned_data={form.cleaned_data}')
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
    

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    model = StatusMessage
    template_name = "mini_fb/delete_status_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the status_message object to the template
        context['status_message'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the profile page after successful deletion
        return reverse('profile_page', kwargs={'pk': self.object.profile.pk})
    
class UpdateStatusMessageView(LoginRequiredMixin, UpdateView):
    model = StatusMessage
    template_name = "mini_fb/update_status_form.html"
    fields = ['message']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the status_message object to the template
        context['status_message'] = self.object
        return context

    def get_success_url(self):
        # Redirect to the profile page after successful deletion
        return reverse('profile_page', kwargs={'pk': self.object.profile.pk})
    

class CreateFriendView(LoginRequiredMixin, View):
    # replace default dispatch
    def dispatch(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=self.request.user)
        other_profile = Profile.objects.get(pk=self.kwargs['other_pk'])
        profile.add_friend(other_profile)        
        return redirect(reverse('profile_page', kwargs={'pk': profile.pk}))
    

class ShowFriendSuggestionsView(DetailView):
    model = Profile
    template_name = "mini_fb/friend_suggestions.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['friend_suggestions'] = self.object.get_friend_suggestions()
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
    
class ShowNewsFeedView(DetailView):
    model = Profile
    template_name = "mini_fb/news_feed.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news_feed'] = self.object.get_news_feed()
        return context
    
    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)
