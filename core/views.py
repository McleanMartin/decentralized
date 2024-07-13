from datetime import timezone
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem, Tenant, Product, Order, OrderItem, Delivery
from .schemas import TenantSchema, ProductSchema, OrderSchema, OrderItemSchema, DeliverySchema ,AddToCartSchema, OrderFromCartSchema
from pydantic import ValidationError
import json

def parse_json_request(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

class TenantView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tenants = list(Tenant.objects.all().values())
        return JsonResponse(tenants, safe=False)

    @csrf_exempt
    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        try:
            schema = TenantSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        tenant = Tenant(**schema.dict(exclude_unset=True))
        tenant.save()
        return JsonResponse(TenantSchema.from_orm(tenant).dict())

    @csrf_exempt
    def put(self, request, pk):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        tenant = get_object_or_404(Tenant, pk=pk)
        try:
            schema = TenantSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(tenant, key, value)
        tenant.save()
        return JsonResponse(TenantSchema.from_orm(tenant).dict())

class ProductView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        products = list(Product.objects.all().values())
        return JsonResponse(products, safe=False)

    @csrf_exempt
    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        try:
            schema = ProductSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        product = Product(**schema.dict(exclude_unset=True))
        product.save()
        return JsonResponse(ProductSchema.from_orm(product).dict())

    @csrf_exempt
    def put(self, request, pk):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        product = get_object_or_404(Product, pk=pk)
        try:
            schema = ProductSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(product, key, value)
        product.save()
        return JsonResponse(ProductSchema.from_orm(product).dict())

class OrderView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = list(Order.objects.all().values())
        return JsonResponse(orders, safe=False)

    @csrf_exempt
    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        try:
            schema = OrderSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        order = Order(**schema.dict(exclude_unset=True))
        order.save()
        return JsonResponse(OrderSchema.from_orm(order).dict())

    @csrf_exempt
    def put(self, request, pk):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        order = get_object_or_404(Order, pk=pk)
        try:
            schema = OrderSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(order, key, value)
        order.save()
        return JsonResponse(OrderSchema.from_orm(order).dict())

class OrderItemView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_items = list(OrderItem.objects.all().values())
        return JsonResponse(order_items, safe=False)

    @csrf_exempt
    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        try:
            schema = OrderItemSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        order_item = OrderItem(**schema.dict(exclude_unset=True))
        order_item.save()
        return JsonResponse(OrderItemSchema.from_orm(order_item).dict())

    @csrf_exempt
    def put(self, request, pk):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        order_item = get_object_or_404(OrderItem, pk=pk)
        try:
            schema = OrderItemSchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(order_item, key, value)
        order_item.save()
        return JsonResponse(OrderItemSchema.from_orm(order_item).dict())

class DeliveryView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        deliveries = list(Delivery.objects.all().values())
        return JsonResponse(deliveries, safe=False)

    @csrf_exempt
    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        try:
            schema = DeliverySchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        delivery = Delivery(**schema.dict(exclude_unset=True))
        delivery.save()
        return JsonResponse(DeliverySchema.from_orm(delivery).dict())

    @csrf_exempt
    def put(self, request, pk):
        data = parse_json_request(request)
        if data is None:
            return Response({"error": "Invalid JSON"}, status=400)
        delivery = get_object_or_404(Delivery, pk=pk)
        try:
            schema = DeliverySchema(**data)
        except ValidationError as e:
            return Response(e.errors(), status=400)
        for key, value in schema.dict(exclude_unset=True).items():
            setattr(delivery, key, value)
        delivery.save()
        return JsonResponse(DeliverySchema.from_orm(delivery).dict())

class CartView(APIView):
    def get(self, request, tenant_id):
        tenant = get_object_or_404(Tenant, id=tenant_id)
        carts = Cart.objects.filter(user=request.user, tenant=tenant, expires_at__gt=timezone.now())
        cart_data = []
        for cart in carts:
            cart_items = CartItem.objects.filter(cart=cart)
            serialized_items = [{'product_id': item.product.id, 'quantity': item.quantity} for item in cart_items]
            cart_data.append({
                'id': cart.id,
                'user': cart.user.email,
                'tenant': cart.tenant.name,
                'created_at': cart.created_at,
                'expires_at': cart.expires_at,
                'items': serialized_items
            })
        return Response(cart_data)

    def post(self, request, tenant_id):
        tenant = get_object_or_404(Tenant, id=tenant_id)
        try:
            data = AddToCartSchema.parse_obj(request.data)
        except ValidationError as e:
            return Response(e.errors(), status=status.HTTP_400_BAD_REQUEST)

        cart, created = Cart.objects.get_or_create(user=request.user, tenant=tenant, expires_at__gt=timezone.now())

        for item_data in data.items:
            product = get_object_or_404(Product, id=item_data.product_id, tenant=tenant)
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += item_data.quantity
            else:
                cart_item.quantity = item_data.quantity
            cart_item.save()

        return Response({'message': 'Items added to cart'}, status=status.HTTP_201_CREATED)

class OrderFromCartView(APIView):
    def post(self, request):
        try:
            data = OrderFromCartSchema.parse_obj(request.data)
        except ValidationError as e:
            return Response(e.errors(), status=status.HTTP_400_BAD_REQUEST)

        cart = get_object_or_404(Cart, id=data.cart_id, user=request.user, expires_at__gt=timezone.now())
        items = CartItem.objects.filter(cart=cart)
        if not items:
            return Response({'message': 'Cart is empty or expired'}, status=status.HTTP_BAD_REQUEST)

        order = Order.objects.create(tenant=cart.tenant, total_amount=0)
        total_amount = 0
        for item in items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity, price=item.product.price)
            total_amount += item.quantity * item.product.price

        order.total_amount = total_amount
        order.save()

        items.delete()
        cart.delete()

        order_data = {
            'id': order.id,
            'created_at': order.created_at,
            'tenant': order.tenant.name,
            'total_amount': order.total_amount,
            'items': [{'product_id': item.product.id, 'quantity': item.quantity, 'price': item.price} for item in order.items.all()]
        }

        return Response(order_data, status=status.HTTP_201_CREATED)