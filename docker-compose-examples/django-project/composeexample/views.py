home()
from django.shortcuts import render
def home(request):
    template = "home.htlm"
    context = {}
    return render (request, template, context)
