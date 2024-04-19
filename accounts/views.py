from django.shortcuts import render
from rest_framework.decorators import api_view
from accounts import services as account_services
from utils.custom_responses import error


@api_view(["POST"])
def signup(request):
    try:
        return account_services.create_user_service(request)
    except Exception as exc:
        return error(message=str(exc))
    

@api_view(["POST"])
def login(request):
    try:
        return account_services.login_user_service(request)
    except Exception as exc:
        return error(message=str(exc))