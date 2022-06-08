from dataclasses import fields
from rest_framework import serializers
from .models import Moviedata

class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'ratings', 'movietype'] 