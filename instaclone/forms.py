from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Image,Profile,Comment

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['user', 'pub_date','comments','likes_counter','like']
        widgets = {
            'id':'form'
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

        
       