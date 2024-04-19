from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from accounts.models import User
from boards.models import Board, Comment


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('boards:index')


@login_required
def follow(request, user_pk) :
    persons = get_user_model()
    person = persons.objects.get(pk=user_pk)
    if request.user != person :
        if request.user in person.followers.all() :
            person.followers.remove(request.user)
        else :
            person.followers.add(request.user)
    return redirect('accounts:profile', user_pk)


@login_required
def profile(request, user_pk) :
    persons = get_user_model()
    boards = Board.objects.all()
    person = persons.objects.get(pk=user_pk)
    boards = person.board_set.all()
    comments = person.comment_set.all()
    followers = person.followers.all()
    likes = person.like_board.all()
    context = {
        'person' : person,
        'boards' : boards,
        'comments' : comments,
        'followers' : followers,
        'likes' : likes,
    }
    return render(request, 'accounts/profile.html', context)