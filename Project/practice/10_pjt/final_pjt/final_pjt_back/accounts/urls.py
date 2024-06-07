from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'user',views.UserViewSet)

app_name = 'accounts'
urlpatterns = [
    path('save-users/', views.save_user, name="save_user"),
    path('current-user/', views.current_user, name='current_user'),
    path('update-financial-products/', views.update_financial_products, name='update_financial_products'),
    path('delete-user/', views.delete_user, name='delete_user'),
    path('update_join_products/', views.update_join_products, name='update_join_products'),
    path('',include(router.urls)),
]