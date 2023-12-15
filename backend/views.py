from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def second_page(request):
    return render(request, 'template/temp1.html')