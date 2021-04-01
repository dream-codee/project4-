from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index1(request):
    return render(request,"hello1.html")

def index2(request):
    return HttpResponse("<h1>C'est t'res bon ici</h1>")