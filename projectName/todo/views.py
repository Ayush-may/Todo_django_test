from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth import login, logout , authenticate 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import TodoForm
from .models import TodoModel

def index(request):
  if request.user.is_authenticated:
    return redirect("todo:list")
  return render(request,'todo/index.html')

def login_user(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if username is None or password is None:
      messages.error(request,"username or password is wrong")
      return redirect("todo:login_user")
    
    user = authenticate(request)
    
    print(user)
    if user is not None:
      login(request , user)
  
    messages.error(request,'user is not available')
    return redirect("todo:index")
  
  return render(request, 'todo/login_user.html')  
  

def create_user(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    
    if User.objects.filter(username = username).exists():
      messages.error(request , 'user is already present.')
      return redirect("todo:login_user")
    
    user = User.objects.create_user(username=username,email=email, password=password)
    messages.success(request,'user is created !')
    
    login(request, user)
    return redirect("todo:list")
    
  return render(request , 'todo/create_user.html')
  
@login_required
def list(request):
  if not request.user.is_authenticated:
    return redirect("todo:index")
  else:
    form = TodoForm()
    todos = TodoModel.objects.filter(user = request.user).all().values()
    
    data = {
      "form" : form,
      "todos" : todos
    }
    
    if request.method == "POST":
      form = TodoForm(request.POST)
      if form.is_valid():
        TodoModel.objects.create(
          content = request.POST.get('content'),
          user = request.user
        )
        # form.save()
        messages.success(request,"todo is added")
        return redirect("todo:list")
        
  return render(request, 'todo/list.html', data)


@login_required
def edit(request, pk):
  todo = get_object_or_404(TodoModel, pk=pk)

  if request.method == "POST":
    form = TodoForm(request.POST, instance=todo)
    if form.is_valid():
      form.save()
      return redirect('todo:list')
  else:
    form = TodoForm(instance=todo)    
    
  return render(request,'todo/edit.html', {
    "form" : form, 'todo' : todo
  })
      
@login_required
def delete(request, pk):
  todo = get_object_or_404(TodoModel, pk=pk)
  
  if request.method == "POST":
    todo.delete()
    messages.success(request, "Todo is deleted")
    return redirect('todo:list')
  
  return render(request,'todo/delete.html',{
    "todo": todo
  })
  
  
def logout_user(request):
  logout(request)
  return redirect("todo:index")