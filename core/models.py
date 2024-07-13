import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class TokenModel(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.token)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    subdomain = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    tenant = models.ForeignKey(Tenant, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tenant = models.ForeignKey(Tenant, related_name='orders', on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Delivery(models.Model):
    order = models.OneToOneField(Order, related_name='delivery', on_delete=models.CASCADE)
    address = models.TextField()
    delivered = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(null=True, blank=True)
