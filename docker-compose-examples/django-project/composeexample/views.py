home()
from django.shortcuts import render
def home(request):
    templatw = "home.htlm"
    context = {}
    return render (request, template, context)
