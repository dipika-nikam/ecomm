
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as login_user, logout
from .models import NewUser
from .forms import Sign_up_form, Login_form
from django.contrib import messages

# Create your views here.

def register(request):
    form = Sign_up_form()
    if request.method == 'POST':
        form = Sign_up_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your email has been successfully registered.")
            return redirect('index')
    context = {
        'form': form
        }
    return render(request, 'register.html', context)

def signin(request):
    form = Login_form()
    if request.method == 'POST':
        username = request.POST['username']
        Password = request.POST['password']

        user = authenticate(request,username = username, password=Password)

        if user is not None:
            login_user(request, user)
            messages.success(request, "Your has been successfully Login.")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')
    context={
        'form': form
    }
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "Your account has been successfully logged out.")
    return redirect('index')


