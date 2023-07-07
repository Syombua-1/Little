from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class MenuSerializer(serializers.ModelSerializer):
    queryset=Menu.objects.all()
    class Meta:
        model = Menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    queryset=Bookingtable.objects.all()
    class Meta:
        model = Bookingtable
        fields = '__all__'
