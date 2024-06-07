from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'products',views.DepositProductsViewSet)

app_name = 'products'
urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products, name="save_deposit_products"),
    path('save-saving-products/', views.save_saving_products, name="save_saving_products"),
    path('get_exchange_rate/',views.get_exchange_rate, name="get_exchange_rate"),
    path('user_join_options/',views.user_join_options, name="user_join_options"),
    path('want_options/',views.want_options, name="want_options"),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_products_options, name="deposit_products_options"),
    path('',include(router.urls)),
    path('recommend/<int:user_id>/',views.recommend_products,name='recommend_products'),
]