from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from parking.models import *
from django.core import serializers
from django.shortcuts import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from datetime import datetime
from datetime import timedelta

@require_http_methods(['GET'])
@csrf_exempt
def park_view(request):
    if request.method == 'GET':
        data={}

        uid=request.GET.get('uid')
        pos_x=request.GET.get('pos_x')
        pos_y=request.GET.get('pos_y')
        status='parked'

        obj = Park.objects.create(uid=uid,pos_x=pos_x,pos_y=pos_y,status=status)
        data['obj']=str(obj.status)
        return JsonResponse(data)

@require_http_methods(['GET'])
@csrf_exempt
def leave_view(request):
    if request.method == 'GET':
        data={}

        uid=request.GET.get('uid')
        query = Park.objects.filter(uid=uid)
        query=query[len(query)-1]
        query.status='left'
        query.save()

        data['query']=str(query.status)
        return JsonResponse(data)


