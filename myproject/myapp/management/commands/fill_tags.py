from django.core.management.base import BaseCommand
from myapp.models import Tag  # Замените 'myapp' на имя вашего приложения

class Command(BaseCommand):
    help = 'Populates the myapp_tag table in PostgreSQL with predefined tags'

    def handle(self, *args, **options):
        tags_data = [
            {'tag_id': 1, 'tag_name': 'shooter'},
            {'tag_id': 2, 'tag_name': 'parkour'},
            {'tag_id': 3, 'tag_name': 'cute'},
            {'tag_id': 4, 'tag_name': 'adventure'},
            {'tag_id': 5, 'tag_name': 'nostalgic'},
            {'tag_id': 6, 'tag_name': 'classic'},
            {'tag_id': 7, 'tag_name': 'puzzle'},
            {'tag_id': 8, 'tag_name': 'sport'},
            {'tag_id': 9, 'tag_name': 'stickman'},
            {'tag_id': 10, 'tag_name': 'vehicle'},
            {'tag_id': 11, 'tag_name': 'clicker'},
            {'tag_id': 12, 'tag_name': 'casual'},
            {'tag_id': 13, 'tag_name': 'action'},
            {'tag_id': 14, 'tag_name': '2 players'},
            {'tag_id': 15, 'tag_name': '1 player'},
        ]

        for data in tags_data:
            Tag.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated myapp_tag table with predefined tags'))
