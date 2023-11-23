# myapp/management/commands/populate_gametags.py

from django.core.management.base import BaseCommand
from myapp.models import GameTag, Tag, Game

class Command(BaseCommand):
    help = 'Populates the myapp_gametag table in PostgreSQL with predefined game-tag relationships'

    def handle(self, *args, **options):
        gametags_data = [
            {'tag_id': 1, 'game_id': 3},
            {'tag_id': 2, 'game_id': 4},
            {'tag_id': 5, 'game_id': 4},
            {'tag_id': 10, 'game_id': 5},
            {'tag_id': 10, 'game_id': 8},
            {'tag_id': 14, 'game_id': 6},
            {'tag_id': 15, 'game_id': 1},
            {'tag_id': 15, 'game_id': 2},
            {'tag_id': 15, 'game_id': 3},
            {'tag_id': 15, 'game_id': 4},
            {'tag_id': 15, 'game_id': 5},
            {'tag_id': 15, 'game_id': 7},
            {'tag_id': 15, 'game_id': 8},
            {'tag_id': 13, 'game_id': 8},
            {'tag_id': 6, 'game_id': 4},
            {'tag_id': 6, 'game_id': 6},
            {'tag_id': 6, 'game_id': 7},
            # Добавьте другие отношения по аналогии
        ]

        for data in gametags_data:
            GameTag.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated myapp_gametag table with predefined game-tag relationships'))
