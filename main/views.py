from drf_multiple_model.views import ObjectMultipleModelAPIView
from product.models import *
from product.serializers import *
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class AboutUsAPIView(APIView):
    """
    О нас
    """
    def get(self, request, format=None):
        about = AboutUs.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(serializer.data)


class AdvantageAPIView(APIView):
    """
    Преимущества
    """
    def get(self, request, format=None):
        advantage = Advantage.objects.all()
        serializer = AdvantageSerializer(advantage, many=True)
        return Response(serializer.data)


class PublicOfferAPIView(APIView):
    """
    Публичная оферта
    """
    def get(self, request, format=None):
        publicoffer = PublicOffer.objects.all()
        serializer = PublicOfferSerializer(publicoffer, many=True)
        return Response(serializer.data)


class SliderAPIView(APIView):
    """
    Слайдер
    """
    def get(self, request, format=None):
        slider = Slider.objects.all()
        serializer = SliderSerializer(slider, many=True)
        return Response(serializer.data)


class HelpAPIView(APIView):
    """
    Помощь
    """
    def get(self, request, format=None):
        help = Help.objects.all()
        serializer = HelpSerializer(help, many=True)
        return Response(serializer.data)


class Help_imgAPIView(APIView):
    
    def get(self, request, format=None):
        help = Help_img.objects.all()
        serializer = Help_imgSerializer(help, many=True)
        return Response(serializer.data)


class Call_backAPIView(CreateAPIView):
    """
    Обратная связь
    """
    queryset = Call_back.objects.all()
    serializer_class = Call_backSerializer


class Footer_first_sideAPIView(APIView):
    """
    Футер
    """
    def get(self, request, format=None):
        footer = Footer_first_side.objects.all()
        serializer = Footer_first_sideSerializer(footer, many=True)
        return Response(serializer.data)


class Main_pageAPIView(ObjectMultipleModelAPIView):
    """
    Главная страница
    """
    querylist = [
        {'queryset': Slider.objects.all(), 'serializer_class': SliderSerializer},
        {'queryset': Product.objects.filter(bestseller=True)[:8], 'serializer_class': ProductSerializer},
        {'queryset': Product.objects.filter(new=True), 'serializer_class': ProductSerializer},
        {'queryset': Collection.objects.all()[:4], 'serializer_class': CollectionSerializer},
        {'queryset': Advantage.objects.all()[:4], 'serializer_class': AdvantageSerializer}
    ]
