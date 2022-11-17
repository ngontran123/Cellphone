from django.urls import path
from ..api.OrderItemApi import OrderItemByOrderDetailView, OrderItemDetailView, OrderItemListView

urlpatterns = [
    path('', OrderItemListView.as_view()),
    path('<int:id>', OrderItemListView.as_view()),
    path('order_detail/<int:order_id>', OrderItemByOrderDetailView.as_view())
]
