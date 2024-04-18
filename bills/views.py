from django.shortcuts import render
from bills import services as bill_service
from rest_framework.decorators import api_view
from utils.custom_responses import error
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView




class ItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        try:
            return bill_service.add_item_service(request)
        except Exception as exc:
            return error("Error in creating item " + exc)


    def put(self, request, item_id):
        try:
            return bill_service.update_item_service(item_id, request)
        except Exception as exc:
            return error("error in updating item " + str(exc))


    def delete(self, request, item_id):
        try:
            return bill_service.delete_item_service(item_id)
        except Exception as exc:
            return error("Error in deleting item " + str(exc))