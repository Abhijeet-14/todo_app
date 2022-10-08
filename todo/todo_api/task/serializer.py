from .models import Task

from rest_framework import serializers


class CreateNewTaskSerializer(serializers.Serializer):
    """Serializer to create a new task"""

    title = serializers.CharField(required=True)
    description = serializers.CharField()
    help = serializers.CharField(default="No")
    priority = serializers.ChoiceField(choices=Task.PRIORITY_CHOICES)


class SingleTaskSerializer(serializers.Serializer):
    """Serializer to create a new task"""

    task_id = serializers.IntegerField(required=True)


class TaskModelSerializer(serializers.ModelSerializer):
    """Task Model Serializer"""

    class Meta:
        model = Task
        fields = "__all__"
