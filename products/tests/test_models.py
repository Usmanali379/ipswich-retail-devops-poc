import pytest
from products.models import Product

@pytest.mark.django_db
def test_product_str():
    p = Product.objects.create(name="Widget", price="9.99")
    assert str(p) == "Widget"