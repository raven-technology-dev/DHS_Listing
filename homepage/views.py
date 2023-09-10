from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.


def homepage(_request:HttpRequest):
    if _request.method=="POST":
        print("Hello, World!")
    return render(_request, "homepage/main.html", {})
