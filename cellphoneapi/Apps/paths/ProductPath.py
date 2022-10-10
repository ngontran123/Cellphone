from django.urls import path
from ..api.ProductApi import ProductList,ProductListDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:Id>', ProductListDetail.as_view()),
]