from django.core.management.base import BaseCommand
from AuthenticationApp.models import CustomUser

class Command(BaseCommand):
    help = "Seeds the database with an admin user"

    def handle(self, *args, **options):
        if not CustomUser.objects.filter(email="admin2@gmail.com").exists():
            CustomUser.objects.create_superuser(
                email="admin2@gmail.com",
                password="123",
                membership="admin",
                username="admin2"
            )
            self.stdout.write(self.style.SUCCESS("✅ Superuser created successfully!"))
        else:
            self.stdout.write(self.style.WARNING("⚠️ Admin user already exists."))
