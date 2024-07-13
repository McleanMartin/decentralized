from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Tenant, Product, Order, OrderItem, Delivery
from .schemas import TenantSchema, ProductSchema, OrderSchema, OrderItemSchema, DeliverySchema
import json
from django.contrib.auth import authenticate, login
from core.utils import generate_token
from django.contrib.auth.decorators import login_required

@method_decorator(csrf_exempt, name='dispatch')
class LoginView(View):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token = generate_token(user)
            return JsonResponse({'token': str(token)})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)


def parse_json_request(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None

@method_decorator([login_required,csrf_exempt], name='dispatch')
class TenantView(View):
    def get(self, request):
        tenants = list(Tenant.objects.all().values())
        return JsonResponse(tenants, safe=False)

    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON")
        schema = TenantSchema(**data)
        tenant = Tenant(**schema.dict(exclude_unset=True))
        tenant.save()
        return JsonResponse(TenantSchema.from_orm(tenant).dict())

@method_decorator([login_required,csrf_exempt], name='dispatch')
class ProductView(View):
    def get(self, request):
        products = list(Product.objects.all().values())
        return JsonResponse(products, safe=False)

    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON")
        schema = ProductSchema(**data)
        product = Product(**schema.dict(exclude_unset=True))
        product.save()
        return JsonResponse(ProductSchema.from_orm(product).dict())

@method_decorator([login_required,csrf_exempt], name='dispatch')
class OrderView(View):
    def get(self, request):
        orders = list(Order.objects.all().values())
        return JsonResponse(orders, safe=False)

    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON")
        schema = OrderSchema(**data)
        order = Order(**schema.dict(exclude_unset=True))
        order.save()
        return JsonResponse(OrderSchema.from_orm(order).dict())

@method_decorator([login_required,csrf_exempt], name='dispatch')
class OrderItemView(View):
    def get(self, request):
        order_items = list(OrderItem.objects.all().values())
        return JsonResponse(order_items, safe=False)

    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON")
        schema = OrderItemSchema(**data)
        order_item = OrderItem(**schema.dict(exclude_unset=True))
        order_item.save()
        return JsonResponse(OrderItemSchema.from_orm(order_item).dict())

@method_decorator([login_required,csrf_exempt], name='dispatch')
class DeliveryView(View):
    def get(self, request):
        deliveries = list(Delivery.objects.all().values())
        return JsonResponse(deliveries, safe=False)

    def post(self, request):
        data = parse_json_request(request)
        if data is None:
            return HttpResponseBadRequest("Invalid JSON")
        schema = DeliverySchema(**data)
        delivery = Delivery(**schema.dict(exclude_unset=True))
        delivery.save()
        return JsonResponse(DeliverySchema.from_orm(delivery).dict())
