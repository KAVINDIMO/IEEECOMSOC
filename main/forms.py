from dataclasses import fields
from django.forms import ModelForm, TextInput, EmailInput,DateInput,NumberInput
from django import forms
from .models import *

class BLOG_FORM(forms.ModelForm):
    class Meta:
        model = blog
        fields = "__all__"

class POSTS_FORM(forms.ModelForm):
    class Meta:
        model = posts
        fields = "__all__"

class EVENT_FORM(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class EVENT_REG(forms.ModelForm):
    class Meta:
        model = event_reg
        fields = "__all__"