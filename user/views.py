from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from user.firebase import auth


class RegistrationAPIView(APIView):
    """
    Регистрация
    """
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        auth.create_user_with_email_and_password(request.data.get('email'),
                                                 request.data.get('password'))

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserAPIView(APIView):
    """
    Вывод всех пользователей
    """
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = self.serializer_class(
            user, context={'request': request}, many=True
            )
        return Response(serializer.data)


class User_detailAPIView(APIView):
    """
    История заказов по юзерам
    """
    permission_classes = (IsAdminUser,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
