from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from workouttracker.quickstart.serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # The queryset determines which objects are to be serialized.
    # In this case, we want to serialize all User objects.
    queryset = User.objects.all().order_by('-date_joined')
    # The serializer_class determines which serializer to use for the User objects.
    # In this case, we want to use the UserSerializer.
    serializer_class = UserSerializer
    # The permission_classes determines which permissions are required to access this view.
    # In this case, we want to require that the user is authenticated.
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # The queryset determines which objects are to be serialized.
    # In this case, we want to serialize all Group objects.
    queryset = Group.objects.all()
    # The serializer_class determines which serializer to use for the Group objects.
    # In this case, we want to use the GroupSerializer.
    serializer_class = GroupSerializer
    # The permission_classes determines which permissions are required to access this view.
    # In this case, we want to require that the user is authenticated.
    permission_classes = [permissions.IsAuthenticated]

