from django.urls import path
from ..api.ProductApi import ProductList, ProductListDetail, ProductNameDetail, ProductByPriceDetail, \
    ProductPaginationDetail, ProductBrandDetail, ProductAvailable

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:id>', ProductListDetail.as_view()),
    path('product_name/<str:pname>', ProductNameDetail.as_view()),
    path('price/<int:from_price>&<int:to_price>', ProductByPriceDetail.as_view()),
    path('paginating/<int:page>&<int:lim>', ProductPaginationDetail.as_view()),
    path('brand/<str:brand_name>', ProductBrandDetail.as_view()),
    path('status/<str:sta>', ProductAvailable.as_view())
]
