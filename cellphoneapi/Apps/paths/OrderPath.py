from django.urls import path
from ..api.OrderApi import OrderListView, OrderDetailListView, OrderOverTimeView

urlpatterns = [
    path('', OrderListView.as_view()),
    path('<int:id>', OrderDetailListView.as_view()),
    path('expire', OrderOverTimeView.as_view())
]
