from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email
import rest_auth.urls
import rest_auth.registration.urls
from django.urls import re_path as url
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cellphone API",
        default_version='v1',
        description="Songoku",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('Apps.paths.ProductPath')),
    path(r'docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('cart/', include('Apps.paths.CartPath')),
    path('cart_item/', include('Apps.paths.CartItemPath')),
    path(r'redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('user/', include('Apps.paths.UserPath')),
    path('order_status/', include('Apps.paths.OrderStatusPath')),
    path('order/', include('Apps.paths.OrderPath')),
    path('product_detail/', include('Apps.paths.ProductDetailPath')),
    path('role/', include('Apps.paths.RolePath')),
    path('order_item/', include('Apps.paths.OrderItemPath'))
]
