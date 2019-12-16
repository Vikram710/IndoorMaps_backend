from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from distro.models import *
from django.core import serializers
from django.shortcuts import HttpResponse
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from datetime import datetime
from datetime import timedelta
#import matplotlib.pyplot as plt


dict1={
    '7-8':0,
    '8-9':0,
    '9-10':0,
    '10-11':0,
    '11-12':0    
}

   
@require_http_methods(['GET'])
@csrf_exempt
def entry(request):
    if request.method == 'GET':
        data={}
        for i in range(1,10):
            for j in range(1,5):
                now = datetime.now()+timedelta(minutes=i*j*2)-timedelta(hours=16)
                now1 = now+ timedelta(minutes=30)
                obj = Dist.objects.create(rp=j, uid=i,exits=now1,enters=now)
                data['response']='sucess'
    return JsonResponse(data)

def stripper(t):
    t=t.replace(microsecond=0,hour=t.hour)
    t=datetime.strftime(t, "%H:%M")
    return t

def stripper1(t):
    min1=(int(t[3])*10+int(t[4]))/60.00
    min1=str(round(min1, 2)).strip('0')
    t=str(t[0])+str(t[1])+str(min1)
    
    return t

def classify(enters,exits):
    enters= stripper1(enters)
    exits= stripper1(exits)
    keys=list(dict1.keys())

    for i in range(len(keys)):
        keys1=keys[i].split('-')
        if float(enters)>float(keys1[0]):
            entrykey=keys1[0]

        if float(exits)<float(keys1[1]):
            exitkey=keys1[1]
            break

    list_keys=[]

    diff=int(exitkey)-int(entrykey)

    for i in range(1,diff+1):
        ran=str(int(entrykey)+1*(i-1))+'-'+str(int(entrykey)+1*i)
        list_keys.append(ran)
        dict1[ran]+=1
        
    return (str(list_keys))


@require_http_methods(['GET'])
@csrf_exempt
def viewv(request):
    if request.method == 'GET':
        data={}
        temp = request.GET.get('rp')
        if temp:
            query = Dist.objects.filter(rp=temp)

            list_entry = [obj.enters for obj in query]
            list_exit = [obj.exits for obj in query]

            for i in range(len(list_entry)):

                d = list_entry[i]
                dex = list_exit[i]

                enters = stripper(d)
                exits = stripper(dex)

                c=classify(enters,exits)

            total = query.count()
            data['total_visits']=total
            data['crowd_freq']=str(dict1)
            #plt.bar(list(dict1.keys()), dict1.values(), color='g')
            #plt.show()

            for keys in dict1:
                dict1[keys]=0


    return JsonResponse(data)

@require_http_methods(['GET'])
@csrf_exempt
def personal(request):
    if request.method == 'GET':
        data={}
        anal={}
        temp = request.GET.get('uid')
        if temp:
            query = Dist.objects.filter(uid=temp)
            list_rp= [obj.rp for obj in query]
            list_entry = [obj.enters for obj in query]
            list_exit = [obj.exits for obj in query]
            
            data['listrp']=str(list_rp)
            
            enterlist=[]
            exitlist=[]
            duration_list=[]

            for i in range(len(list_entry)):

                d = list_entry[i]
                dex = list_exit[i]

                enters = stripper(d)
                exits = stripper(dex)

                enterlist.append(enters)
                exitlist.append(exits)
            
            for i in range(len(list_entry)):
            
                FMT = '%H:%M'
                tdelta = (datetime.strptime(exitlist[i], FMT) - datetime.strptime(enterlist[i], FMT)).seconds/3600

                duration_list.append(tdelta)         
                anal[list_rp[i]]=(enterlist[i],exitlist[i],tdelta)
                print(anal[list_rp[i]])
                

            data['duration']=str(anal)

            labels = list_rp
            sizes = duration_list
            colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red','violet','grey','navy','yellow']
            patches, texts = plt.pie(sizes, colors=colors,labels=labels)
            #plt.axis('equal')
            #plt.tight_layout()
            #plt.show()


    return JsonResponse(data)


