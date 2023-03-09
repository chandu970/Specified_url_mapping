from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def RRR(request):
    return HttpResponse('<h1 style="background-color:pink;">This is Film Most Famous</h1>')

def warrior(request):
    return HttpResponse('<h1 style="background-color:orange;">The warrior Director  is N. Lingusamy</h1>')