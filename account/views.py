from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import LoginForm, UserRegistrationForm, ProfileEditForm, UserEditForm
from .models import Profile

from django.contrib import messages


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
                    messages.success(request, 'Siz tizimga kirdigiz!')
                    return redirect('main')
                else:
                    messages.error(request, 'Your account is not active')
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

def user_dashboard(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/dashboard/main_dashboard.html', context)


def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            Profile.objects.create(user=new_user)
            context = {
                "new_user": new_user
            }
            return render(request, 'users/signup_done.html', context)
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form
        }
        return render(request, 'users/signup.html', context)
def singup_done(request):
    user_form = UserRegistrationForm()
    context = {'user_form': user_form}
    return render(request, 'users/signup_done.html', context)


# def edit_user(request):
#     if request.method == "POST":
#         user_form = UserEditForm(data=request.user, instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
#     context = {
#         "user_form": user_form,
#         "profile_form": profile_form
#     }
#     return render(request, 'users/edit_user.html', context)

def edit_user(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = Profile(user=user)

    if request.method == "POST":
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Siz malumotlar o\'zgartirildi!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Siz malumotlar o\'zgartirilmadi!')
            return redirect('edit_user')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = ProfileEditForm(instance=profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, 'users/dashboard/edit_user.html', context)