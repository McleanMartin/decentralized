from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import TenantView, ProductView, OrderView, OrderItemView, DeliveryView

app_name = 'core'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/tenants/', TenantView.as_view(), name='tenant-list'),
    path('api/tenants/<int:pk>/', TenantView.as_view(), name='tenant-detail'), 
    path('api/products/', ProductView.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductView.as_view(), name='product-detail'),
    path('api/orders/', OrderView.as_view(), name='order-list'),
    path('api/orders/<int:pk>/', OrderView.as_view(), name='order-detail'),
    path('api/order-items/', OrderItemView.as_view(), name='orderitem-list'),
    path('api/order-items/<int:pk>/', OrderItemView.as_view(), name='orderitem-detail'), 
    path('api/deliveries/', DeliveryView.as_view(), name='delivery-list'),
    path('api/deliveries/<int:pk>/', DeliveryView.as_view(), name='delivery-detail'),
]
