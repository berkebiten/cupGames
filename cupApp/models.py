from django.db import models
from django.utils import timezone


class Account(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1)
    coins = models.IntegerField(default=500)
    level = models.IntegerField(default=1)
    type = models.CharField(max_length=2, default="FU")
    about_text = models.TextField(blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now())
    isPremium = models.BooleanField(default=False)
    playLimit = models.IntegerField(default=15)
    last_visit_date = models.DateTimeField(default=timezone.now())
    warn_value = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    profile_pic = models.CharField(max_length=1500, null=True, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=25, primary_key=True)
    play_count = models.BigIntegerField()
    thumbnail = models.CharField(max_length=1500)

    def __str__(self):
        return self.category_name


class Game(models.Model):
    game_name = models.CharField(max_length=200, primary_key=True)
    thumbnail = models.CharField(max_length=1500)
    about_text = models.TextField()
    how_to_play_text = models.TextField()
    link = models.CharField(max_length=1500, blank=True, null=True)
    added_date = models.DateTimeField(default=timezone.now())
    play_count = models.BigIntegerField()
    category1 = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cat_1', blank=True, null=True)
    category2 = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cat_2', blank=True, null=True)
    category3 = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name='cat_3', blank=True, null=True)

    def __str__(self):
        return self.game_name


class Score(models.Model):
    username = models.ForeignKey(Account, related_name='score_owner', on_delete=models.CASCADE)
    game_name = models.ForeignKey(Game, related_name='score_game', on_delete=models.CASCADE)
    score = models.BigIntegerField()
    score_date = models.DateTimeField(default=timezone.now())

    def __int__(self):
        return self.score


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    username = models.ForeignKey(Account, related_name='comment_owner', on_delete=models.CASCADE)
    game_name = models.ForeignKey(Game, related_name='comment_game', on_delete=models.CASCADE)
    text = models.TextField()

    def __int__(self):
        return self.comment_id


class Statistic(models.Model):
    username = models.ForeignKey(Account, related_name='statistic_owner', on_delete=models.CASCADE)
    game_name = models.ForeignKey(Game, related_name='statistic_game', on_delete=models.CASCADE)
    play_count = models.IntegerField()
    average_score = models.BigIntegerField()
    last_score = models.BigIntegerField()
    rank = models.IntegerField()


class Badge(models.Model):
    username = models.ForeignKey(Account, related_name='badge_owner', on_delete=models.CASCADE)
    game_name = models.ForeignKey(Game, related_name='badge_game', on_delete=models.CASCADE, null=True, blank=True)
    badge_name = models.CharField(max_length=50)
    is_owned = models.BooleanField()
    thumbnail = models.CharField(max_length=1500)

    def __str__(self):
        return self.badge_name


class Suggestion(models.Model):
    username = models.ForeignKey(Account, related_name='suggestion_owner', on_delete=models.DO_NOTHING, null=True, blank=True)
    detail = models.TextField()
    submit_time = models.DateTimeField(default=timezone.now())
    last_modified = models.DateTimeField(default=timezone.now())
    is_checked = models.BooleanField()
    is_starred = models.BooleanField()
    suggestion_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.suggestion_id


class Favorite(models.Model):
    username = models.ForeignKey(Account, related_name='favourite_owner', on_delete=models.CASCADE)
    game_name = models.ForeignKey(Game, related_name='favourite_game', on_delete=models.CASCADE)
    favoriteId = models.AutoField(primary_key=True)

    def __int__(self):
        return self.favoriteId
