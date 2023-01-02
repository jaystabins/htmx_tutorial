from django.urls import path
from items.views import (
    ItemCreateView, 
    ItemDetailView, 
    ItemListView,
    ItemDeleteView,  
    ItemUpdateView,
    item_dashboard
) 


urlpatterns = [
    path("", item_dashboard, name='item-dashboard'),
    path("list/", ItemListView.as_view(), name="item-list"),
    path("create/", ItemCreateView.as_view(), name="item-create"),
    path("<pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
    path("<pk>/edit/", ItemUpdateView.as_view(), name="item-update"),
    path("<pk>/", ItemDetailView.as_view(), name="item-detail"),
]
