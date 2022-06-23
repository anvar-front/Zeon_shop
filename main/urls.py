from django.urls import path
from main.views import *


urlpatterns = [
    path('about_us', AboutUsAPIView.as_view()),
    path('advantage', AdvantageAPIView.as_view()),
    path('slider', SliderAPIView.as_view()),
    path('public_offer', PublicOfferAPIView.as_view()),
    path('help', HelpAPIView.as_view()),
    path('call_back', Call_backAPIView.as_view()),
    path('footer', Footer_first_sideAPIView.as_view())
]