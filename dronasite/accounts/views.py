from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from home.models import streams

# Create your views here.

def register(request):

    stream = streams.objects.all()

    return render(request, "register.html", {'streams': stream})