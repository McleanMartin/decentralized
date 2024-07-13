# # core/admin.py
# from django.contrib import admin
# from .models import Supermarket, TokenModel, Product, Order, OrderItem, Delivery

# @admin.register(Supermarket)
# class SupermarketAdmin(admin.ModelAdmin):
#     list_display = ('name', 'subdomain')
#     search_fields = ('name', 'subdomain')

# @admin.register(TokenModel)
# class TokenModelAdmin(admin.ModelAdmin):
#     list_display = ('user', 'token', 'created')
#     search_fields = ('user__username', 'token')
#     readonly_fields = ('token', 'created')

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'supermarket', 'price', 'stock')
#     search_fields = ('name', 'supermarket__name')
#     list_filter = ('supermarket',)

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:  # Restrict non-superusers to their supermarket's products
#             queryset = queryset.filter(supermarket=request.user.profile.supermarket)  # Assuming you have a profile model linked to user
#         return queryset

# class OrderItemInline(admin.TabularInline):
#     model = OrderItem
#     extra = 1

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('supermarket', 'created_at', 'total_amount')
#     search_fields = ('supermarket__name',)
#     list_filter = ('supermarket', 'created_at')
#     inlines = [OrderItemInline]

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:  # Restrict non-superusers to their supermarket's orders
#             queryset = queryset.filter(supermarket=request.user.profile.supermarket)  # Assuming you have a profile model linked to user
#         return queryset

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity', 'price')
#     search_fields = ('order__supermarket__name', 'product__name')

# @admin.register(Delivery)
# class DeliveryAdmin(admin.ModelAdmin):
#     list_display = ('order', 'address', 'delivered', 'delivery_date')
#     search_fields = ('order__supermarket__name', 'address')
#     list_filter = ('delivered', 'delivery_date')

#     def get_queryset(self, request):
#         queryset = super().get_queryset(request)
#         if not request.user.is_superuser:  # Restrict non-superusers to their supermarket's deliveries
#             queryset = queryset.filter(order__supermarket=request.user.profile.supermarket)  # Assuming you have a profile model linked to user
#         return queryset
