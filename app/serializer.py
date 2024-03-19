from rest_framework import serializers
from .models import User
from .models import Projects
from .models import Task
class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['id', 'user_id', 'first_name']
    
class ProjectsSerializer(serializers.Serializer):
    user = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=100)
    
class Task(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    desc = serializers.CharField(max_length=100)
    user = serializers.IntegerField()
    date = serializers.DateField()
    status = serializers.CharField(max_length = 50)
    project = serializers.IntegerField()