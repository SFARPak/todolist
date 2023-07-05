import csv, io
import string, random
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

# Create your views here.
from .models import List
from . forms import ListModelForm, MyUserForm

@login_required
def index(request):
    qs = List.objects.all()
    context = {
        'title': 'Home',
            'todo_list': qs,
        }
    return render(request,'list/index.html', context ) 

@login_required
def user_profile(request, slug):
    list = get_object_or_404(List, slug=slug)
    qs = List.objects.all()
    context = {
        'list_list': qs,
        'list' : list,
        'description':'Adding New Todo to Directory | Todo List',
        'keywords': ['todo', 'directory', 'django', 'python']
        }
    return render(request, 'directory/user-profile.html', context)

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@login_required
def list_add(request):
    qs = List.objects.all()
    form = ListModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        messages.success(request, 'Todo Added.')
        form = ListModelForm()
    else:
        messages.error(request, '')
    context = {
        'form' : form,
        'todo_list': qs,
        'title': 'Adding New Todo to Directory',
        'description':'Adding New Todo to Directory | Todo List',
        'keywords': ['list', 'list', 'django', 'python']
    }
    return render(request, 'list/list-add.html', context)

@login_required
def list_update(request, slug):
    obj = get_object_or_404(List, slug=slug)
    form = ListModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Todo Updated.')
    context = {
        "title": f"Update {obj.title}",
        'form' : form,
        'description':'Updating List | Todo List',
        'keywords': ['todo', 'list', 'django', 'python']
        }
    return render(request, 'list/list-update.html', context)

@login_required
def list_delete(request, slug):
    obj = ListModelForm(List, slug=slug)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Todo Deleted.')
        return redirect('')
    context = {
        'object' : obj,
        'blog_title' : List.title,
        'description':'Deleting Todo from List | Todo List',
        'keywords': ['todo', 'list', 'django', 'python']
    }
    return render(request, 'list/list-delete.html', context)

def form(request):
    form = ListModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListModelForm()
    
    context = {
                'title': 'List input form',
                'form': form
        }

    return render(request,'list/form.html', context )

def register_view(request):
    form = MyUserForm()
    if request.method=='POST':
        form = MyUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created.')
    context = {'form': form}
    return render(request,'list/register.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request,'list/login.html')