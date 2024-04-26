from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/detail/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:movie_pk>/detail/<int:comment_pk>/delete_comment/', views.delete_comment, name='delete_comment'),
    path('<int:movie_pk>/likes/', views.likes_movie, name='likes_movie'),
    path('<int:movie_pk>/<int:comment_pk>/likes/', views.likes_comment, name='likes_comment'),
]
