from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Exchange, Weekend, Holiday
import six


class ExchangeSerializer(serializers.HyperlinkedModelSerializer):
    timezone = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.username')
    weekend = serializers.StringRelatedField(many=True, read_only=True)
    holidays = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Exchange
        fields = (
            'url',
            'ticker',
            'id',
            'name',
            'location',
            'timezone',
            'opening_time',
            'closing_time',
            'weekend',
            'holidays',
            'owner'
        )

    def get_timezone(self, obj):
        return six.text_type(obj.timezone)


class UserSerializer(serializers.ModelSerializer):
    exchanges = serializers.HyperlinkedRelatedField(queryset=Exchange.objects.all(),
                                                    view_name='exchange-detail',
                                                    many=True)

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'exchanges')
