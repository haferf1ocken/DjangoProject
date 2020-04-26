from rest_framework import serializers
from .models import Deal


class DealListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'


class DealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'
