from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def all(request):
    data = Lecuture.objects.all()
    data = list(data.values())

    context = {'list': data}
    return render(request, 'lecturelist/entirelist.html', context)

def opening(request):
    return render(request, 'lecturelist/openlist.html')

def funding(request):
    return render(request, 'lecturelist/fundinglist.html')

def detail(request, list_id):
    lecture = Lecuture.objects.get(pk=list_id)
    context = { 'lecture': lecture }
    return render(request, 'lecturelist/detail.html', context)
