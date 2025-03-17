from django.core.management.base import BaseCommand
from faker import Faker
from shopApp.models import Contacts

fake = Faker('es_ES')  # Configuramos Faker para español

class Command(BaseCommand):
    help = "Genera 30 contactos falsos en la base de datos"

    def handle(self, *args, **kwargs):
        for _ in range(30):
            Contacts.objects.create(
                full_name=fake.name(),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.email(),
                active=True
            )
        self.stdout.write(self.style.SUCCESS("✅ 30 contactos generados correctamente"))
