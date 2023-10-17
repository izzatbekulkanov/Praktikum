from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('main')
                else:
                    return HttpResponse('Your account is not active.')
            else:
                return HttpResponse('Invalid username and/or password.')
        else:
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'users/login.html', context)

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('main')
def user_signup(request):

    return render(request, 'users/signup.html')
def user_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/dashboard/dashboard.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            context = {
                "new_user": new_user
            }
            return render(request, 'users/signup_done.html', context)
        else:
            user_form = UserRegistrationForm()
            print(user_form)
            context = {
                "user_form": user_form
            }
            return render(request, 'users/signup.html', context)
def singup_done(request):
    user_form = UserRegistrationForm()
    context = {'user_form': user_form}
    return render(request, 'users/signup_done.html', context)
