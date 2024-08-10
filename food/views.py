from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'food/index.html', {'items': items})


def item_detail(request, id):
    item = Item.objects.get(id=id)
    return render(request, 'food/detail.html', {'item': item})


@login_required
def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('food:item_list')
    else:
        form = ItemForm()

    return render(request, 'food/item-form.html', {'form': form}) 
    

def update_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('food:item_list')
    else:
        form = ItemForm()

    return render(request, 'food/item-form.html', {'form':form, 'item':item})        


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:item_list')
    
    return render(request, 'food/item-delete.html', {'item': item})        
