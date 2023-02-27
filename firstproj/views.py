from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Page')

def home(request):
    return render(request, 'home.html', {'greeting':'Hello home page'})