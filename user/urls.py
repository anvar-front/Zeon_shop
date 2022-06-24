from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import *

app_name = 'user'

urlpatterns = [
    path('', UserAPIView.as_view()),
    path('<int:pk>', User_detailAPIView.as_view(), name='user-detail'),
    path('reg', RegistrationAPIView.as_view()),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
