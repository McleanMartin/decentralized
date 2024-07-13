from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    subdomain = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('client', 'Client'),
        ('developer', 'Developer'),
        ('driver', 'Driver'),
        ('manager', 'Manager'),
        ('administration', 'Administration'),
    )

    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default='client')
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


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
