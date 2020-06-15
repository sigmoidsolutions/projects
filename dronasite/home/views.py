from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import streams
# Create your views here.


def home(request):
    stream1 = streams()
    stream1.id = "1"
    stream1.title = "Science"
    stream1.img = "science.jpg"

    stream2 = streams()
    stream2.id = "2"
    stream2.title = "Medical"
    stream2.img = "medical.jpg"

    stream3 = streams()
    stream3.id = "3"
    stream3.title = "Commerce"
    stream3.img = "commerce.jpg"

    stream = [stream1,stream2,stream3]

    return render(request, "index.html", {'streams': stream})
