from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import streams
# Create your views here.


def home(request):

    stream = streams.objects.all()

    return render(request, "index.html", {'streams': stream})
