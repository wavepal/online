from django.core.management.base import BaseCommand
from myapp.models import Game  # Замените 'your_app' на имя вашего приложения

class Command(BaseCommand):
    help = 'Populates the online_games table in PostgreSQL'

    def handle(self, *args, **options):
        games_data = [
            {'game_id': 2, 'game_name': '2048', 'filename': '2048', 'description': '2048 - это браузерная игра, которая объединяет в себе элементы математики и головоломки! Игровой процесс заключается в объединении плиток номиналом «2», которые при слитии образуют значение их суммы. Цель игры - получить плитку номиналом «2048» (2 в 11 степени). Удачи!', 'release_date': '2014-01-14', 'developer_name': 'Габриэле Чирулли', 'imagename': '2048.png'},
            {'game_id': 3, 'game_name': 'Coronavirus Shooter', 'filename': 'corona', 'description': 'Copyright (c) 2023 by Faisal Jawed (https://codepen.io/faisal-jawed/pen/NWqeRNZ)', 'release_date': '2023-11-19', 'developer_name': 'Faisal Jawed', 'imagename': 'corona.png'},
            {'game_id': 4, 'game_name': 'Doodle Jump', 'filename': 'doodlejump', 'description': 'Doodle Jump — аркадный экшен-платформер с видом сбоку. вам предстоит путешествовать по листу миллиметровой бумаги, постоянно прыгая с одной платформы на другую, собирая реактивные ранцы, избегая черных дыр и взрывая злодеев шариками в носу. Вы получите удовольствие, пролетая мимо реальных маркеров рекордных очков других игроков, нацарапанных на полях. Эта игра безумно затягивает.', 'release_date': '2023-11-19', 'developer_name': 'Игорь и Марко Пусеняки', 'imagename': 'doodlejump.jpg'},
            {'game_id': 5, 'game_name': 'Enduro - Atari', 'filename': 'enduro', 'description': 'Игра про гонки.', 'release_date': '2023-11-19', 'developer_name': 'rafaelcastrocouto', 'imagename': 'enduro.png'},
            {'game_id': 6, 'game_name': 'Ping-Pong', 'filename': 'pingpong', 'description': 'Игра на два игрока', 'release_date': '2023-11-19', 'developer_name': '8wave', 'imagename': 'pingpong.png'},
            {'game_id': 7, 'game_name': 'Snake', 'filename': 'snake', 'description': 'Игра про змейку которая ест яблоки', 'release_date': '2023-11-19', 'developer_name': 'Snake Productions', 'imagename': 'snake.png'},
            {'game_id': 8, 'game_name': 'Rockets', 'filename': 'rockets', 'description': 'Игра про две ракеты, победи компьютер используя свою ракету и уклоняйся от метеоритов!', 'release_date': '2023-11-19', 'developer_name': 'Rocket Pics', 'imagename': 'rockets.png'},
        ]

        for data in games_data:
            Game.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Successfully populated online_games table'))