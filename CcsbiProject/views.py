from django.shortcuts import render

# Create your views here.
def CcsbiProject(request):
    return render(request,'index.html',{})
