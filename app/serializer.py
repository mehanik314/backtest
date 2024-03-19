from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=100)
    
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