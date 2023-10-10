from django.shortcuts import render, get_object_or_404

# Create your views here.


def main(request):
    return render(request, 'base/main.html')
def error404(request):
    return render(request, 'pages/404.html')
def contact(request):
    return render(request, 'pages/contact.html')
def single_page(request):
    return render(request, 'pages/single_page.html')
