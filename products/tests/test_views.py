import pytest

from products.models import Product


@pytest.mark.django_db
def test_product_list_view(client):
    Product.objects.create(name="A", price="1.00")
    res = client.get("/")
    assert res.status_code == 200
    assert b"Products" in res.content
