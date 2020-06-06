from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from home.forms import homeForm
# Create your views here.


def home(request):
    return render(request, "index.html")

    def get(request):
        getSearchKey = request.POST["search"]
        print(getSearchKey)