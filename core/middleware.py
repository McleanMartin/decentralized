# shop/middleware.py
from django.db import connection
from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Tenant

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        subdomain = self.get_subdomain(request)
        
        try:
            tenant = Tenant.objects.get(subdomain=subdomain)
        except ObjectDoesNotExist:
            return JsonResponse({'tenant error':'Tenant not register'})

        request.tenant = tenant
        response = self.get_response(request)
        return response

    def get_subdomain(self, request):
        """
        Extracts subdomain from request HTTP_HOST.
        """
        return request.META.get('HTTP_HOST', '').split('.')[0]
