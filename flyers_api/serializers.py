from django.contrib.auth.models import User, Group
from .models import Flyer
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Group
        fields = ('url', 'name')

class FlyerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Flyer
        fields = ('street', 'city', 'state')
