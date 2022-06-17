# from rest_framework import status
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .renderers import UserJSONRenderer

# from .models import *
# from .serializers import *

# from rest_framework_simplejwt.views import TokenObtainPairView


# class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer


# class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):

#         serializer = self.serializer_class(
#             request.user, data=request.data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class RegistrationAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UserList(APIView):
#     permission_classes = (AllowAny,)
#     serializer_class = UserSerializer

#     def get(self, request, format = None):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many = True)
#         return Response(serializer.data)