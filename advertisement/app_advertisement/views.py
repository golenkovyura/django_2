from django.shortcuts import render
from .models import Advertisement


def index(request):
    advertisements = Advertisement.objects.all()  # Список всех объявлений в БД 
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)


def top_sellers(request):
    return render(request, 'top-sellers.html')
