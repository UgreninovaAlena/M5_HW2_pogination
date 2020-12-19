from pprint import pprint
import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


def get_content(path):
    colum_name = ['ID', 'Name', 'Street', 'District']
    content = []

    with open(path, newline='\n', encoding='cp1251') as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=";")

        for elem in file_reader:
            content_elem = {}

            for colum in colum_name:
                content_elem[colum] = elem[colum]

            content.append(content_elem)

    return content

CONTENT = get_content(settings.FILES_PATH)


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = int(request.GET.get('page', 1))

    paginator = Paginator(CONTENT, settings.ITEMS_ON_PAGE)
    page = paginator.get_page(current_page)

    next_page_url = None
    if page.has_next():
        number_next_page = page.next_page_number()
        next_page_url = reverse('bus_stations') + f'?page={number_next_page}'

    prev_page_url = None
    if page.has_previous():
        number_prev_page = page.previous_page_number()
        prev_page_url = reverse('bus_stations') + f'?page={number_prev_page}'

    return render(request, 'index.html', context={
        'bus_stations': page.object_list,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })
