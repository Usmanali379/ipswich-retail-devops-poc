from django.core.management.base import BaseCommand

from products.models import Product

SAMPLE = [
    {
        "name": "Eco Bottle",
        "price": "12.99",
        "description": "Reusable BPA-free water bottle.",
        "image_url": "https://picsum.photos/seed/bottle/600/400",
    },
    {
        "name": "Canvas Tote",
        "price": "19.50",
        "description": "Durable tote bag for everyday use.",
        "image_url": "https://picsum.photos/seed/tote/600/400",
    },
    {
        "name": "Notebook A5",
        "price": "6.00",
        "description": "A5 dot grid notebook – 120 pages.",
        "image_url": "https://picsum.photos/seed/notebook/600/400",
    },
    {
        "name": "Wireless Mouse",
        "price": "24.90",
        "description": "Ergonomic mouse with silent clicks.",
        "image_url": "https://picsum.photos/seed/mouse/600/400",
    },
    {
        "name": "Desk Lamp",
        "price": "34.00",
        "description": "LED lamp with adjustable arm.",
        "image_url": "https://picsum.photos/seed/lamp/600/400",
    },
    {
        "name": "Coffee Mug",
        "price": "9.75",
        "description": "Ceramic mug 350ml.",
        "image_url": "https://picsum.photos/seed/mug/600/400",
    },
]


class Command(BaseCommand):
    help = "Seed a handful of sample products"

    def handle(self, *args, **kwargs):
        created = 0
        for p in SAMPLE:
            obj, was_created = Product.objects.get_or_create(
                name=p["name"],
                defaults={
                    "description": p["description"],
                    "price": p["price"],
                    "image_url": p["image_url"],
                },
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} products."))
