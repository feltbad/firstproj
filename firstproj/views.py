from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Page')

def home(request):
    return render(request, 'home.html', {'greeting':'Hello home page'})

def reverse(request):
    text_area = request.GET['textarea']
    count_words = len(text_area.split())
    reversed_text = text_area[::-1]
    return render(request, 'reverse.html', {'textarea':text_area, 'reversedtext':reversed_text, 'countwords':count_words})