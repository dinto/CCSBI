from django.shortcuts import render

# Create your views here.
def CcsbiProject(request):
    return render(request,'index.html',{'navbar':'home'})

def contact(request):
    return render(request,'contact.html',{'navbar':'contact'})

def project(request):
    return render(request,'Projects.html',{'navbar':'project'})

def Networks(request):
    return render(request,'Networks.html',{'navbar':'network'})
def Datasets(request):
    return render(request,'Datasets.html',{'navbar':'dataset'})
def Resources(request):
    return render(request,'Resources.html',{'navbar':'resource'})
def Capacity(request):
    return render(request,'Capacity.html',{'navbar':'capacity'})
def Events(request):
    return render(request,'Events.html',{'navbar':'event'})
def Opportunities(request):
    return render(request,'Opportunities.html',{'navbar':'opportunities'})
def Event1(request):
    return render(request,'Event1.html',{'navbar':'event'})