from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo



# Create your views here.
def home(request):
    return render(request, 'posts/index.html')

def add_todo(request):
    return HttpResponseRedirect("/")
