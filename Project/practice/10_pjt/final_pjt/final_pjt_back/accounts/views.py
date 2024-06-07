from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.conf import settings
from .serializers import UserSerializers
from django.contrib.auth import get_user_model
from products.models import DepositProducts, DepositOptions

# Create your views here.
@api_view(["GET", "POST"])
def save_user(request) :
    User = get_user_model()
    users = User.objects.all()
    if request.method == "POST" :
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid() :
            user = User.objects.create_user(username=serializer.data['username'],
                                            nickname=serializer.data['nickname'],
                                            email=serializer.data['email'],
                                            age=serializer.data['age'],
                                            money=serializer.data['money'],
                                            salary=serializer.data['salary'],
                                            password=serializer.data['password'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET" :
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)
    
class UserViewSet(viewsets.ModelViewSet):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class  = UserSerializers

@api_view(["GET", "PUT"])
def current_user(request) :
    user = request.user
    if request.method == "GET" :
        if user.is_authenticated:
            serializer = UserSerializers(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.method == "PUT" :
        serializer = UserSerializers(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_financial_products(request):
    user = request.user
    financial_products = request.data.get('financial_products', [])
    user.financial_products.set(financial_products)
    user.save()
    serializer = UserSerializers(user)
    return Response(serializer.data)


@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_join_products(request) :
    user = request.user
    join_product_ids = request.data.get('join_products', [])
    join_products = DepositOptions.objects.filter(id__in=join_product_ids)
    user.join_products.set(join_products)
    user.save()
    serializer = UserSerializers(user)
    return Response(serializer.data)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user(request):
    user = request.user
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)