from django.urls import path
from ..api.CartItemsApi import CartItemList, CartItemByCartIdDetail, CartItemIdDetail

urlpatterns = [
    path('', CartItemList.as_view()),
    path('<int:id>', CartItemIdDetail.as_view()),
    path('cart_id/<int:cart_id>', CartItemByCartIdDetail.as_view())
]
