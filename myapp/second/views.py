from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>Tech with tim</h1>")

def about(response):
    return HttpResponse("<h1>This is an About us page</h1>")