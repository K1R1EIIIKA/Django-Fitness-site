from django.shortcuts import render

from .models import Offer


def home(request):
    offers = Offer.objects.all()

    data = {
        'offers': offers
    }

    return render(request, 'main/home.html', data)
