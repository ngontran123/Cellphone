from django.urls import path
from ..api.UserApi import Register, Login, UserDetail, Logout, UserDetailByResfresh, UserViewList

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('user', UserDetail.as_view()),
    path('logout', Logout.as_view()),
    path('refresh', UserDetailByResfresh.as_view()),
    path('list', UserViewList.as_view())
]
