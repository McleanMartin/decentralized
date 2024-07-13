# shop/urls.py
from django.urls import path
from .views import TenantView, ProductView, OrderView, OrderItemView, DeliveryView,LoginView

app_name = 'core'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('supermarkets/', TenantView.as_view()),
    path('products/', ProductView.as_view()),
    path('orders/', OrderView.as_view()),
    path('order-items/', OrderItemView.as_view()),
    path('deliveries/', DeliveryView.as_view()),
]
