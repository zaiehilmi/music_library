from rest_framework import serializers
from base.models import MusicLibrary

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MusicLibrary
        fields = '__all__'