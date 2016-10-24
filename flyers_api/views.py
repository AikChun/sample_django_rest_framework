import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User, Group
from .models import Flyer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, FlyerSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset         = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset         = Group.objects.all()
    serializer_class = GroupSerializer

class FlyerFilter(django_filters.rest_framework.FilterSet):
    state = django_filters.CharFilter(name="state", lookup_expr='iexact');
    class Meta:
        model = Flyer
        fields = ['street', 'city', 'state',]

class FlyerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset         = Flyer.objects.all()
    serializer_class = FlyerSerializer
    filter_backends  = (DjangoFilterBackend,)
    filter_class     = FlyerFilter

