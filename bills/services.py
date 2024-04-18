from rest_framework.decorators import api_view
from bills import repository as bill_repo
from utils.custom_responses import success, error, ok, unauthorized


def add_item_service(request):
    try:
        bill_repo.create_item(request.data)
        return success(message="Item created succesfully")
    except Exception as exc:
        return error(message="Error in creating item " + str(exc))
        

def update_item_service(item_id, request):
    try:
        bill_repo.update_item(item_id, request.data)
        return success(message="Item updated succesfully")
    except Exception as exc:
        return error(message="Error in updaing item "+ str(exc))

def delete_item_service(item_id):
    try:
        bill_repo.delete_item(item_id)
        return ok(message="Item deleted succesfully")
    except Exception as exc:
        return error(message="Error in deleting item "+ str(exc))