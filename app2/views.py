from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def CEO(request):
    return HttpResponse('<h1 style="background-color:tomato;"><marquee style="color:blue;"> New Film of Ram charan is Ceo</marquee></h1> ')

def AA(request):
    return HttpResponse('<h1 style="background-color:skyblue;"><span style="color:brown;">This is the Film of Nithin</span></h1>')