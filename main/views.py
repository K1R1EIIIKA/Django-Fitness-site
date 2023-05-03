from django.shortcuts import render

from .models import Offer


def home(request):
    offers = Offer.objects.all()

    data = {
        'offers': offers
    }

    return render(request, 'main/home.html', data)


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def instructors(request):
    return render(request, 'main/instructors.html')


def policy(request):
    return render(request, 'main/policy.html')
