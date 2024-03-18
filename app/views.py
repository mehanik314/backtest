from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Projects
from .models import User



def Projects_Data(request):

    data = Projects.project_desc
    return JsonResponse(data, safe=False)



def User_Data(request):
    data = request.GET.get('user_id')
    return HttpResponse('id: ' + str(data))

def Hello(request):
    return HttpResponse('Hello')