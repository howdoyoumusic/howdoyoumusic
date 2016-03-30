'''
Forms for user and profile create and edit.
'''
import datetime

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.forms.extras.widgets import SelectDateWidget
from django.forms.models import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as __
from django.utils import timezone
from django.template import loader

from . import models

class UserForm(ModelForm):
    '''
    This is used for profile edit form
    '''
    required_css_class = 'required'

    first_name = forms.CharField(max_length=250) 
    last_name = forms.CharField(max_length=250)
    cell_phone = forms.IntegerField()
    email = forms.EmailField()
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for key in self.fields:
            self.fields[key].required = True

    def save(self, commit=True):
        instance = super(UserForm, self).save(commit=False)

        user = self.initial['user']
        print user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.cell_phone = self.cleaned_data['cell_phone']
        user.save()

        skills = self.cleaned_data['skills']
        print skills
        for skill in skills:
            instance.skills.add(skill)

        instance.user = user
        if commit:
            instance.save()

        return instance

    class Meta:
        model = models.UserProfile
        fields = ['user_photo', 'skills']
        labels = {
            'cell_phone': __('Phone Number'),
            'email': __('Email'),
        }

class MediaUploadForm(ModelForm):
    def save(self, commit=True):
        instance = super(MediaUploadForm, self).save(commit=False)
        user = self.initial['user']

        instance.user = user
        if commit:
            instance.save()

        return instance

    class Meta:
        model = models.UserMedia
        fields = ['name', 'media_type', 'media_url']
        labels = {
            'media_type': __('File Type'),
            'media_url': __('Upload File'),
        }