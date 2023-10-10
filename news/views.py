from django.shortcuts import render, get_object_or_404

# Create your views here.


def base(request):
    return render(request, 'base/base.html')
