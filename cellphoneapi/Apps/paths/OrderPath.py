from django.urls import path
from ..api.OrderApi import OrderListView, OrderDetailListView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:id>', OrderDetailListView.as_view())
]
