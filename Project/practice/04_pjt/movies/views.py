from django.shortcuts import render, redirect
from .models import Movie, Comment
from .forms import MovieForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request) :
    movies = Movie.objects.all()
    context = {
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request) :
    if request.method == "POST" :
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid() :
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:index')
    else :
        form = MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html', context)


def detail(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    comment_form = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie' : movie,
        'comment_form' : comment_form,
        'comments' : comments,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def update(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    if request.user == movie.user :
        if request.method == "POST" :
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid() :
                change = form.save(commit=False)
                change.user = movie.user
                change.save()
                return redirect('movies:detail', movie.pk)
        else :
            form = MovieForm(instance=movie)
    else :
        return redirect('movies:index')
    context = {
        'form' : form,
        'movie' : movie,
    }
    return render(request, 'movies/update.html', context)


@login_required
def delete(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()
    return redirect('movies:index')


@login_required
def create_comment(request, movie_pk) :
    movie = Movie.objects.get(pk=movie_pk)
    if request.method == "POST" :
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid() :
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()
    return redirect('movies:detail', movie.pk)

@login_required
def delete_comment(request, movie_pk, comment_pk) :
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user :
        comment.delete()
    return redirect('movies:detail', movie_pk)