from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet, CommentViewSet
from . import views

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'comments', CommentViewSet)

app_name = 'articles'
urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.article_list, name='article_list'),
    path('delete_article/<int:articleId>/', views.delete_article, name='delete_article'),
    path('article_update/<int:articleId>/', views.article_update, name='article_update'),
    path('update_like_users/<int:articleId>/', views.update_like_users, name='update_like_users'),
    path('<int:articleId>/comment/', views.comment, name='comment'),
    path('<int:articleId>/update_comment/<int:commentId>/', views.update_comment, name='update_comment'),
]