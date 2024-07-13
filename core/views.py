from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tenant, Product, Order, OrderItem, Delivery
from .schemas import TenantSchema, ProductSchema, OrderSchema, OrderItemSchema, DeliverySchema
from pydantic import ValidationError
import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Product, Cart, CartItem, Order, OrderItem, Tenant
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
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
