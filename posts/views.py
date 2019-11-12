from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils import timezone
from .models import Todo



# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by('-added_date')
    return render(request, 'posts/index.html', {'todo_items': todo_items})

@csrf_exempt
def add_todo(request):
    added_date = timezone.now()
    content = request.POST['content']
    Todo.objects.create(added_date=added_date, text=content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
