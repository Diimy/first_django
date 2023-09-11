from http.client import HTTPResponse
from django.shortcuts import render

def abc(request):
    return HTTPResponse("fljçwak")
