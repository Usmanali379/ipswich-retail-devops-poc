from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    items = Product.objects.all().order_by("name")
    return render(request, "products/product_list.html", {"items": items})

def product_detail(request, pk: int):
    item = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"item": item})