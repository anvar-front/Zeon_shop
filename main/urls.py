from django.urls import path
from main.views import *
from main.views import *


urlpatterns = [
    path('about_us', AboutUsAPIView.as_view()),
    path('advantage', AdvantageAPIView.as_view()),
    path('slider', SliderAPIView.as_view()),
    path('public_offer', PublicOfferAPIView.as_view()),
    path('help', HelpAPIView.as_view()),
    path('help_img', Help_imgAPIView.as_view())
]