from rest_framework import serializers
from .models import NewGeneratorData

class NewGeneratorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewGeneratorData
        fields = '__all__' 