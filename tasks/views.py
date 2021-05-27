

from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
# Create your views here.
from tasks.forms import TaskForm
from tasks.models import Task


def index(request):
    return HttpResponse('Hello')

# class TaskList(ListView):
#     template_name = 'list.html'
#     queryset = Task.objects.all()
#

class TaskList(View):
    template_name = 'list.html'
    def get(self, request, *args, **kwargs):
        context ={
            'object_list': Task.objects.all(),
            'form': TaskForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            form = TaskForm(None)
        context ={
            'object_list': Task.objects.all(),
            'form': form
        }
        return redirect(reverse('tasks:list'))
        #return render(request, self.template_name, context)

class TaskUpdate(View):
    template_name = 'update.html'
    def get(self, request, my_id=None, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        form = TaskForm(instance=task)

        context = {
            'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request, my_id=None, *args, **kwargs):
        task = Task.objects.get(id=my_id)
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            form = TaskForm()
        return redirect(reverse('tasks:list'))

class TaskDelete(View):
    template_name = 'delete.html'

    def get(self, request, my_id=None, *args, **kwargs):

        return render(request, self.template_name, {'obj': Task.objects.get(id=my_id)})

    def post(self, request, my_id=None, *args, **kwargs):
        obj = Task.objects.get(id=my_id)
        obj.delete()
        return redirect(reverse('tasks:list'))