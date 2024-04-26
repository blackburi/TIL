from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm) :
    class Meta :
        model = Movie
        fields = '__all__'
        exclude = ('user',)


class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ('content',)