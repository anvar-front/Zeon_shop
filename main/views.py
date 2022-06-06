from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import CreateAPIView
from drf_multiple_model.views import ObjectMultipleModelAPIView
from .models import *
from .serializers import *

from product.models import *
from product.serializers import *


class AboutUsAPIView(APIView):

    def get(self, request, format=None):
        about = AboutUs.objects.all()
        serializer = AboutUsSerializer(about, many=True)
        return Response(serializer.data)


class AdvantageAPIView(APIView):

    def get(self, request, format=None):
        advantage = Advantage.objects.all()
        serializer = AdvantageSerializer(advantage, many=True)
        return Response(serializer.data)


class PublicOfferAPIView(APIView):
    
    def get(self, request, format=None):
        publicoffer = PublicOffer.objects.all()
        serializer = PublicOfferSerializer(publicoffer, many=True)
        return Response(serializer.data)


class SliderAPIView(APIView):

    def get(self, request, format=None):
        slider = Slider.objects.all()
        serializer = SliderSerializer(slider, many=True)
        return Response(serializer.data)


class HelpAPIView(APIView):
    
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

    queryset = Call_back.objects.all()
    serializer_class = Call_backSerializer


class Footer_first_sideAPIView(APIView):

    def get(self, request, format=None):
        footer = Footer_first_side.objects.all()
        serializer = Footer_first_sideSerializer(footer, many=True)
        return Response(serializer.data)


class Main_pageAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Slider.objects.all(), 'serializer_class': SliderSerializer},
        {'queryset': Product.objects.filter(bestseller=True)[:8], 'serializer_class': ProductSerializer},
        {'queryset': Product.objects.filter(new=True), 'serializer_class': ProductSerializer},
        {'queryset': Collection.objects.all()[:4], 'serializer_class': CollectionSerializer},
        {'queryset': Advantage.objects.all()[:4], 'serializer_class': AdvantageSerializer}
    ]