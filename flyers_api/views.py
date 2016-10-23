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

class FlyerList(APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get(self, request):
        flyers = Flyer.objects.all()
        serializer = FlyerSerializer(flyers, many=True)
        return Response(serializer.data)

    def post(self):
        pass







