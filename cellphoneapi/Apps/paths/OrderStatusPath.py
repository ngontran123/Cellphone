from django.urls import path
from ..api.OrderStatusApi import OrderStatusListView, OrderStatusByName

urlpatterns = [
    path('', OrderStatusListView.as_view()),
    path('<str:name>', OrderStatusByName.as_view())
]
