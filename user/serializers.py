from rest_framework import serializers

from .models import User
from cart.models import Client
from cart.serializers import ClientSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации
    """
    class Meta:
        model = User
        fields =['email', 'password']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Для вывода всех юзеров
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='user:user-detail',
        lookup_field='pk'
    )

    class Meta:
        model = User
        fields = ['id', 'url', 'email']


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Детализация для получения историю закаов по юзерам
    """
    orders = serializers.SerializerMethodField('get_orders')

    class Meta:
        model = User
        fields = ['id', 'email', 'orders']

    def get_orders(self, obj):
        order = Client.objects.filter(user=obj.id)
        order_data = ClientSerializer(order, many=True)
        return order_data.data