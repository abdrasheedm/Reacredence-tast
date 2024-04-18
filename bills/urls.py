from django.urls import path
from . import views


urlpatterns = [
    path('add-item', views.ItemView.as_view(), name='add_item'),
    path('update-item/<str:item_id>', views.ItemView.as_view(), name='update_item'),
    path('delete-item/<str:item_id>', views.ItemView.as_view(), name='delete_item'),
]