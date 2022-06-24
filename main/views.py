from product.models import *
from product.serializers import *
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import *
from .serializers import *


class AboutUsAPIView(APIView):
    """
    О нас
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        about = AboutUs.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(serializer.data)


class AdvantageAPIView(APIView):
    """
    Преимущества
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        advantage = Advantage.objects.all()
        serializer = AdvantageSerializer(advantage, many=True)
        return Response(serializer.data)


class PublicOfferAPIView(APIView):
    """
    Публичная оферта
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        publicoffer = PublicOffer.objects.all()
        serializer = PublicOfferSerializer(publicoffer, many=True)
        return Response(serializer.data)


class SliderAPIView(APIView):
    """
    Слайдер
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        slider = Slider.objects.all()
        serializer = SliderSerializer(slider, many=True)
        return Response(serializer.data)


class HelpAPIView(APIView):

    def get(self, request, format=None):
        help = Help_img.objects.all()
        serializer = Help_imgSerializer(help, many=True)
        return Response(serializer.data)


class Call_backAPIView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    """
    Обратная связь
    """
    queryset = Call_back.objects.all()
    serializer_class = Call_backSerializer


class Footer_first_sideAPIView(APIView):
    """
    Футер
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        footer = Footer_first_side.objects.all()
        serializer = Footer_first_sideSerializer(footer, many=True)
        return Response(serializer.data)
