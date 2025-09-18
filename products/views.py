from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Product


def product_list(request):
    q = request.GET.get("q", "").strip()
    qs = Product.objects.all().order_by("name")
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(qs, 9)  # 9 per page
    page = request.GET.get("page")
    items = paginator.get_page(page)
    return render(request, "products/product_list.html", {"items": items, "q": q})


def product_detail(request, pk: int):
    item = get_object_or_404(Product, pk=pk)
    return render(request, "products/product_detail.html", {"item": item})
