from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from user.firebase import auth


class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        new = auth.create_user_with_email_and_password(request.data.get('email'), request.data.get('password'))
        print(new)
        print(request.data.get('email'))
        print()
        print(request.data.get('password'))

        return Response(serializer.data, status=status.HTTP_201_CREATED)
