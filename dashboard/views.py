from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductAdd, OrderForm
from django.contrib.auth.models import User

@login_required
def index(request):
    order = Order.objects.all()
    product = Product.objects.all()
    itemcount = Product.objects.all().count
    staffcount = User.objects.all().count
    ordercount = Order.objects.all().count
    
    if(request.method == 'POST'):
        form = OrderForm(request.POST)
        if(form.is_valid):
            instance = form.save(commit = False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
        
    context = {
        'order' : order,
        'product' : product,
        'form' : form,
        'staffcount' : staffcount,
        'itemcount' : itemcount,
        'ordercount' : ordercount,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    staff = User.objects.all()
    staffcount = staff.count()
    ordercount = Order.objects.all().count
    itemcount = Product.objects.all().count
    
    context = {
        'staff' : staff,
        'staffcount' : staffcount,
        'itemcount' : itemcount,
        'ordercount' : ordercount,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staffDetail(request, pk):
    staff = User.objects.get(id = pk)
    
    context = {
        'staff' : staff,
    }
    return render(request, 'dashboard/staff-detail.html', context)

@login_required
def product(request):
    items = Product.objects.all()
    itemcount = items.count()
    staffcount = User.objects.all().count
    ordercount = Order.objects.all().count
    
    if(request.method == "POST"):
        form = ProductAdd(request.POST)
        if(form.is_valid):
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductAdd()
        
    context = {
        'items' : items,
        'itemcount' : itemcount,
        'form' : form,
        'staffcount' : staffcount,
        'ordercount' : ordercount,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def productDelete(request, pk):
    item = Product.objects.get(id = pk)
    if(request.method == "POST"):
        item.delete()
        return redirect('dashboard-product')
    
    return render(request, 'dashboard/product-delete.html')

@login_required
def productUpdate(request, pk):
    item = Product.objects.get(id = pk)
    if(request.method == "POST"):
        form = ProductAdd(request.POST, instance = item)
        if(form.is_valid):
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductAdd(instance = item)
        
    context = {
        'form' : form,
    }
    return render(request, 'dashboard/product-update.html', context)

@login_required
def order(request):
    order = Order.objects.all()
    ordercount = order.count()
    staffcount = User.objects.all().count
    itemcount = Product.objects.all().count
    
    context = {
        'order' : order,
        'ordercount' : ordercount,
        'staffcount' : staffcount,
        'itemcount' : itemcount,
    }
    return render(request, 'dashboard/order.html', context)