from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import *
from .serializers import *


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