from dataclasses import field
from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    about_img = serializers.StringRelatedField(many=True)

    class Meta:
        model = AboutUs
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantage
        fields = '__all__'


class PublicOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    # slider_img = serializers.StringRelatedField(many=True)
    class Meta:
        model = Slider
        fields = '__all__'


class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = '__all__'
        

class Help_imgSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)
    class Meta:
        model = Help_img
        fields = ['image', 'questions']