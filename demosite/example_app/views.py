# Create your views here.
from django.shortcuts import render
from example_app.models import Person

def home(request):
    return render(request,
                  'home.html')


