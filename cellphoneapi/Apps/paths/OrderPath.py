from django.urls import path
from ..api.OrderApi import OrderListView

urlpatterns = [
    path('', OrderListView.as_view())
]
