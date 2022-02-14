from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.core.paginator import Paginator


def index(request):
    response = requests.get("https://www.hetzner.com/a_hz_serverboerse/live_data.json")
    data = response.json()['server']
    p = Paginator(data, 20)
    pn = request.GET.get('page')
    page_obj = p.get_page(pn)

    context = {
        'data': data,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)
