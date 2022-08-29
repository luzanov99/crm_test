from asyncio import tasks
from django.shortcuts import render
from rest_framework import viewsets, status, permissions, generics
from tasks.serializers import UserTaskSerializer
from tasks.models import Task
from rest_framework.viewsets import ModelViewSet

class UserTaskViewSet(ModelViewSet):
    serializer_class = UserTaskSerializer

    def get_queryset(self):
        return Task.objects.filter(responsible=self.request.user.pk)
