from django.urls import path
from . import views

urlpatterns = [
    path('age_nearest/', views.age_nearest),
    path('average_test/', views.average_test),
]

