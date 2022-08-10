from django import forms
from .models import Blogs


class Blogforms(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
        exclude = ['is_approved', 'user']
