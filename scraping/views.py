from django.shortcuts import render
from .models import Vacancy


def home_view(request):
    qs = Vacancy.objects.all()
    return render(request, 'scraping/home.html', context={'object_list': qs})
