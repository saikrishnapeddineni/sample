from django.http import HttpResponse
from django.shortcuts import render

def a (request):
    return HttpResponse("Hi This is medical college")
def z(request):
    return render(request,'fee/k.html')
