from django.urls import path
from ..api.OrderStatusApi import OrdreStatusListView,OrderStatusByName

urlpatterns = [
    path('', OrdreStatusListView.as_view()),
    path('<str:name>',OrderStatusByName.as_view())
]
