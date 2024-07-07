from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.db import connections

class Command(BaseCommand):
    help = 'Create a default superuser if one does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Debugging output to check database connection
        self.stdout.write(self.style.SUCCESS(f'Database connection settings: {connections.databases}'))
        
        if not User.objects.filter(username='defaultadmin').exists():
            User.objects.create_superuser(
                username='admins',
                email='admin@examples.com',
                password='snipher8431'
            )
            self.stdout.write(self.style.SUCCESS('Successfully created default superuser'))
        else:
            self.stdout.write('Default superuser already exists')
