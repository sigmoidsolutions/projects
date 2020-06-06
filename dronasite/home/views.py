from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import searchForm
# Create your views here.


def home(request):
    submitbutton= request.POST.get("submit")

    getKey=''

    form= searchForm(request.POST or None)
    if form.is_valid():
        getKey= form.cleaned_data.get("searchkey")


    context= {'form': form, 'searchkey': getKey,}

    return render(request, "index.html", context)
