from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user = authenticate(request,
                                username=data['username'],
                                password=data['password'])
            print(user.password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Muvaffaqiyatli login amalga oshirildi")
                else:
                    return HttpResponse("Profilingiz faol holatda emas")
            else:
                return HttpResponse("Login yoki parol hato")
    else:
        form = LoginForm()
        context = {
            "form": form
        }
    return render(request, 'user/login.html', context)

def user_logout(request):
    logout(request)
    return render(request, 'user/logout.html') # Sizning asosiy sahifangizga o'tkazadi, 'main' o'rniga o'zingizning sahifangizning nomini qo'yishingiz kerak
