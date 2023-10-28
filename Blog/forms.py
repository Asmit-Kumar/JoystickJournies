from django import forms
from . import models as m


class PostForm(forms.ModelForm):
    class Meta:
        model = m.Post
        fields = [
            'title',
            'body',
            'publish',
            'genres',
            'status',
            ]
        