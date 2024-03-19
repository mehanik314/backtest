from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from rest_framework.decorators import api_view, renderer_classes
from django.core.exceptions import ObjectDoesNotExist
import sqlite3
from .models import Projects
from .models import User
from .serializer import UserSerializer
from .serializer import ProjectsSerializer
from .serializer import TaskSerializer
def get_user_data(user_id):
    try:
        user = User.objects.get(user_id=user_id)
        return user
    except ObjectDoesNotExist:
        return None
    
    
def exist_user(user_id):
    try:
        user = User.objects.filter(user_id=user_id).exists()
        return user
    except ObjectDoesNotExist:
        return None
    
    
    
def project_exists(userid):
    userobj = User.objects.get(user_id=userid)
    project_exists = Projects.objects.filter(user_id = userobj).exists()
    return project_exists


@require_GET
def Projects_Data(request):
    get_id = request.GET.get('user_id')
    title="заглушка title"
    if exist_user(get_id):
        project_exists_value = project_exists(get_id)
        if project_exists_value == False:
            try:
                user = User.objects.get(user_id=get_id)
                project = Projects.objects.create(user_id = user, title=title)
            except Exception as e:
                print(f"Error creating user: {e}")
            serializer = ProjectsSerializer(project)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                user = User.objects.get(user_id=get_id)
                project = Projects.objects.filter(user_id=user)
                serializer = ProjectsSerializer(project, many=True)
                return JsonResponse(serializer.data, safe=False)
            except Projects.DoesNotExist:
                return JsonResponse({'error': 'Project not found'}, status=404)
            except Exception as e:
                print(f"Error retrieving project: {e}")
                return JsonResponse({'error': 'Error retrieving project'}, status=500)
    else:
        User_Data(request)
        return JsonResponse({'error': 'пользователь не найден'}, status=500)


        
@require_GET
def User_Data(request):
    get_id = request.GET.get('user_id')
    first_name = "заглушка"
    user = get_user_data(get_id)
    if not user:
        try:
            user = User.objects.create(user_id=get_id, first_name=first_name)
        except Exception as e:
             print(f"Error creating user: {e}")
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    else:
        user = User.objects.get(user_id = get_id)
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data, safe=False)
    
@require_GET
def Hello(request):
    return HttpResponse('Hello')