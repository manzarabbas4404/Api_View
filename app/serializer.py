from rest_framework import serializers
from .models import *


class studentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = students
        fields = ['id','name','age','city']