from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm) :
    grade = forms.FloatField(min_value=0, max_value=5, step_size=0.5, required=False)
    class Meta :
        model = Movie
        fields = '__all__'
        exclude = ('user',)


class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ('content',)