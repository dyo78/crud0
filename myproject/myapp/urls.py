from django.urls import path
from .views import UserDetail,CustomUserInfo

urlpatterns = [
    path("user/", UserDetail.as_view(), name='user'),
    path("user/<int:id>/", CustomUserInfo.as_view(), name="customuser-info"),
]
