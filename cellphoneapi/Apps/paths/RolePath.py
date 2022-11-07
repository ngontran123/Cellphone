from django.urls import path
from ..api.RoleApi import RoleListView, RoleApiView, RoleNameApiView

urlpatterns = [
    path('', RoleListView.as_view()),
    path('<int:id>', RoleApiView.as_view()),
    path('role_name/<str:name>', RoleNameApiView.as_view())
]
