from django.db import models
from django.contrib.auth.models import User
class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    release_date = models.DateField()
    developer_name = models.CharField(max_length=255)
    imagename = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag, through='GameTag')

    def __str__(self):
        return self.game_name

class GameTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tag.tag_name} - {self.game.game_name}'

class Liked(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.game.game_name}"