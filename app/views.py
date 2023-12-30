from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def create_topic(request):
    if request.method=='POST':
        tname=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tname)[0]
        TO.save()
        return HttpResponse('topic table created ')
    return render(request,'create_topic.html')

def create_webpage(request):
    if request.method=='POST':
        tname=request.POST['tn']
        wn=request.POST['n']
        ur=request.POST['u']
        em=request.POST['e']

        TO=Topic.objects.get_or_create(topic_name=tname)[0]
        WO=Webpage.objects.get_or_create(topic_name=TO,name=wn,url=ur,email=em)[0]
        WO.save()
        return HttpResponse('webpage is created')
    
    return render(request,'create_webpage.html')