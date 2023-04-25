from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'pearl_safaris/home.html',{})
