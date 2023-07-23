from django.core.management.base import BaseCommand, CommandError
from faker import Faker

class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.faker = Faker('en_GB') # set to British English
         
    def handle(self, *args, **options):
        print("WARNING: The SEED command has not been implemented yet.")
