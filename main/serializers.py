from dataclasses import field, fields
from statistics import mode
from rest_framework import serializers
from .models import *


class AboutUsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для страницы "О нас"
    """
    about_img = serializers.StringRelatedField(many=True)

    class Meta:
        model = AboutUs
        fields = "__all__"


class AdvantageSerializer(serializers.ModelSerializer):
    """
    Сериализатор для преимуществ
    """
    class Meta:
        model = Advantage
        fields = '__all__'


class PublicOfferSerializer(serializers.ModelSerializer):
    """
    Сериализтор для страницы 'Публичная оферта'
    """
    class Meta:
        model = PublicOffer
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для слайдера
    """
    class Meta:
        model = Slider
        fields = ['link', 'image']


class HelpSerializer(serializers.ModelSerializer):
    """
    Помощь
    """
    class Meta:
        model = Help
        fields = '__all__'


class Help_imgSerializer(serializers.ModelSerializer):
    questions = serializers.StringRelatedField(many=True)

    class Meta:
        model = Help_img
        fields = ['image', 'questions']


class Call_backSerializer(serializers.ModelSerializer):
    """
    Обратная связь
    """
    class Meta:
        model = Call_back
        fields = ['name', 'phone_number', 'type', 'date']


class Footer_second_sideSerializer(serializers.ModelSerializer):
    social = serializers.StringRelatedField()

    class Meta:
        model = Footer_second_side
        fields = ['social', 'link']


class Footer_first_sideSerializer(serializers.ModelSerializer):
    """
    Футер
    """
    link = Footer_second_sideSerializer(many=True)

    class Meta:
        model = Footer_first_side
        fields = ['number', 'logo', 'info', 'link']
