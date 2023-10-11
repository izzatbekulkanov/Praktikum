from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.


def main(request):
    return render(request, 'base/main.html')
def error404(request):
    return render(request, 'pages/404.html')



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Sahifani qaytarish uchun 'return' ishlatish
            return render(request, 'base/main.html')  # 'main' o'rniga o'zingizning shabloningizni qo'yishingiz kerak
    else:
        form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'pages/contact.html', context)

def single_page(request):
    return render(request, 'pages/single_page.html')
