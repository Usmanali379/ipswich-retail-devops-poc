from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def healthz(request):
    return HttpResponse("ok", content_type="text/plain")

def metrics(request):
    return HttpResponse(generate_latest(), content_type=CONTENT_TYPE_LATEST)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("products.urls")),
    path("cart/", include("cart.urls")),
    path("healthz", healthz),
    path("metrics", metrics),
]