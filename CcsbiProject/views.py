from django.shortcuts import render

# Create your views here.
def CcsbiProject(request):
    return render(request,'index.html',{})

def contact(request):
    return render(request,'contact.html',{})

def project(request):
    return render(request,'Projects.html',{})

def Networks(request):
    return render(request,'Networks.html',{})
def Datasets(request):
    return render(request,'Datasets.html',{})
def Resources(request):
    return render(request,'Resources.html',{})
def Capacity(request):
    return render(request,'Capacity.html',{})
def Events(request):
    return render(request,'Events.html',{})
def Opportunities(request):
    return render(request,'Opportunities.html',{})
def Event1(request):
    return render(request,'Event1.html',{})