from django.shortcuts import render
from .models import Item


def item_list(request):
    items = Item.objects.all()
    return render(request, 'food/index.html', {'items': items})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'food/detail.html', {'item': item})
