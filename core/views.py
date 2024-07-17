from django.shortcuts import render

def index(request):
    return render(request, 'core/inicio.html')
# Create your views here.
