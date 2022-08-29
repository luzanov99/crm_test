from rest_framework import serializers
from tasks.models import Task


class UserTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ["id","name", "date","responsible", "create_date",]