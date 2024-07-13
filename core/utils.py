# core/utils.py
from core.models import TokenModel
from django.contrib.auth.models import User
import uuid

def generate_token(user):
    token, created = TokenModel.objects.get_or_create(user=user)
    return token.token
