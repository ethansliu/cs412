from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):

    firstName = forms.CharField(label="First Name", required=True)
    lastName = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.EmailField(label="Email", required=True)
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        '''associate this form witht he Comment model'''
        model = Profile
        fields = ['firstName', 'lastName', 'city', 'email', 'image_url']



class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create Comment data.'''

    class Meta:
        '''associate this form witht he Comment model'''
        model = StatusMessage
        # fields = ['article', 'author', 'text', ]
        # remove the article because we want to do this automagically
        fields = ['message',]