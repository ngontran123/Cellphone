from django.urls import path
from ..api.CartApi import CartList, CartListDetail, CartByUserName

urlpatterns = [
    path('', CartList.as_view()),
    path('<int:id>', CartListDetail.as_view()),
    path('username/<str:username>', CartByUserName.as_view())
]
