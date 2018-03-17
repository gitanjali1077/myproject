from rest_framework import serializers
from .models import urls

class urlsSerializer(serializers.ModelSerializer):

    class Meta:
        model = urls
        fields='__all__'
