from django.urls import path

from .apps import UsersConfig
from .views import MyTokenObtainPairView, UserCreateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserCreateAPIView.as_view(), name='user_create'),
]