from django.shortcuts import render
from django.http import HttpResponse

#create views here

def index(request):
    return HttpResponse("success")
