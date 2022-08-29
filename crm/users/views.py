from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from users.models import Group, Role
from users.serializers import RoleSerializer, GroupSerializer
from users.permissions import IsAdmin

class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdmin]


class RoleViewSet(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    #permission_classes = [IsAdmin]