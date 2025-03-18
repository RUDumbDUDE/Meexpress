from django.core.management.base import BaseCommand
from shopApp.models import Contact
from faker import Faker

class Command(BaseCommand):
    help = "Genera 30 contactos ficticios"

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(30):
            Contact.objects.create(
                full_name=fake.name(),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.email(),
                active=fake.boolean(chance_of_getting_true=70),  # 70% de probabilidad de ser activo
            )
        self.stdout.write(self.style.SUCCESS("¡30 contactos generados con éxito!"))


