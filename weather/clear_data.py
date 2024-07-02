from django.core.management.base import BaseCommand


class Command(BaseCommand):
    hep = 'Clear application data or resets application state'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Suvcessfully cleared'))