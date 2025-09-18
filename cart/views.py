from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product

from .models import CartItem


def cart_view(request):
    items = CartItem.objects.all()
    total = sum(i.line_total() for i in items)
    return render(request, "cart/cart.html", {"items": items, "total": total})


def add_to_cart(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    CartItem.objects.create(product=product, quantity=1)
    return redirect("/cart/")
