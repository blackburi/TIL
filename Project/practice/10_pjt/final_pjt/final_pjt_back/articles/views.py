from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Article, Comment
from .serializers import ArticleSerializer, CommentSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated])
def article_update(request,articleId):
    article = get_object_or_404(Article, pk=articleId)
    if request.method == "DELETE" :
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT" :
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_like_users(request, articleId) :
    user = request.user
    article = Article.objects.get(id=articleId)
    if user in article.like_users.all() :
        article.like_users.remove(user)
    else :
        article.like_users.add(user)
    return Response(status=status.HTTP_200_OK)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_article(request, articleId) :
    article = get_object_or_404(Article, pk=articleId)
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def comment(request, articleId) :
    article = get_object_or_404(Article, pk=articleId)
    if request.method == 'GET' :
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT", "DELETE"])
def update_comment(request, articleId, commentId) :
    article = Article.objects.get(pk=articleId)
    comment = Comment.objects.get(article=article, id=commentId)
    if request.method == "DELETE" :
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT" :
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)