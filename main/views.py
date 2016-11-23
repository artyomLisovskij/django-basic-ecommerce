from django.shortcuts import render
from .models import *

def home(request):
    template_name = 'home.html'
    context = {
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)
    
    
def view_category(request, slug):
    template_name = 'category.html'
    category = Category.objects.filter(slug=slug)
    context = {
        'items': Item.objects.filter(category=category),
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)
    
    
def view_item(request, category_slug, item_slug):
    template_name = 'item.html'
    category = Category.objects.get(slug=category_slug)
    item = Item.objects.get(slug=item_slug, category=category)
    context = {
        'slug2': item_slug,
        'category': category,
        'item': item,
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)
    
    
def cart(request):
    template_name = 'cart.html'
    ids = request.GET.get('ids','')
    ids = ids.split(',')
    array_cart = []
    total = 0
    for idx in ids:
        if idx !='':
            item = Item.objects.get(id=idx)
            total = total + item.price
            array_cart.append({'title':item.title, 'price':item.price, 'id':item.id})
    context = {
        'ids':ids,
        'cart':array_cart,
        'total':total,
        'categories': Category.objects.all()
    }
    return render(request, template_name, context)