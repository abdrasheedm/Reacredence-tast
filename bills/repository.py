from bills.models import Item



def create_item(data):
    try:
        Item.objects.create(**data)
    except Exception as exc:
        raise Exception("Error in creating item" + str(exc))
    

def update_item(item_id, data):
    try:
        if Item.objects.filter(id=item_id).exists():
            Item.objects.update(**data)
    except Exception as exc:
        raise Exception("Error in updating item" + str(exc))
    

def delete_item(item_id):
    try:
        if Item.objects.filter(id=item_id).exists():
            Item.objects.get(id=item_id).delete()
    except Exception as exc:
        raise Exception("Error in deleting item" + str(exc))