from pprint import pprint
import csv
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


# --------------------------------------------------------------------------------------------------
# КУСОК КОДА АНАЛОГИЧЕН, НО В settings ОН РАБОТАЕТ А ТУТ НЕТ
def get_content(path):
    colum_name = ['ID', 'Name', 'Street', 'District']
    content = []

    with open(path, newline='', encoding='cp1251') as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=",")
        print(f'>>>{file_reader}')
        for elem in file_reader:

            content_elem = {}
            for colum in colum_name:
                content_elem[colum] = elem[colum]
            content.append(content_elem)

    return content


CONTENT = get_content(settings.FILES_PATH)
pprint(CONTENT)
# --------------------------------------------------------------------------------------------------

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    # current_page = int(request.GET.get('page', 1))
    #
    # paginator = Paginator([1,2,3,4,5,6,7,8,9,10,11], settings.ITEMS_ON_PAGE)
    # page = paginator.get_page(current_page)
    # pprint(page.object_list)
    # pprint(CONTENT)

    next_page_url = 'write your url'

    # return render(request, 'index.html', context={
    #     'bus_stations': page.object_list,
    #     'current_page': current_page,
    #     'prev_page_url': None,
    #     'next_page_url': next_page_url,
    # })

    return render(request, 'index.html', context={
        'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'},
                         {'Name': 'другое название', 'Street': 'другая улица', 'District': 'другой район'}],
        'current_page': current_page,
        'prev_page_url': None,
        'next_page_url': next_page_url,
    })

