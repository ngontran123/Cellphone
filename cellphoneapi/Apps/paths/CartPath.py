from django.urls import path
from ..api.CartApi import CartList, CartListDetail, CartByUserName, DeleteOrUpdateView

urlpatterns = [
    path('', CartList.as_view()),
    path('<int:id>', CartListDetail.as_view()),
    path('username', CartByUserName.as_view()),
    path('delete', DeleteOrUpdateView.as_view())
]
