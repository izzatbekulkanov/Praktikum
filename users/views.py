from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm
def custom_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('some_redirect_url')  # Kirish qilingan foydalanuvchi bosh sahifaga yo'naltiriladi

    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('some_redirect_url')  # Ro'yhatdan o'tgan foydalanuvchi bosh sahifaga yo'naltiriladi

    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})