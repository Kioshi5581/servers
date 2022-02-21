from django.shortcuts import render
import requests
from django.core.paginator import Paginator


def index(request):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
    }
    url = "https://www.hetzner.com/a_hz_serverboerse/live_data.json"
    response = requests.get(url, headers=headers)
    data = response.json()['server']
    p = Paginator(data, 20)
    pn = request.GET.get('page')
    print(pn, p, data)
    page_obj = p.get_page(pn)

    context = {
        'data': data,
        'page_obj': page_obj
    }
    return render(request, 'index.html', context)
