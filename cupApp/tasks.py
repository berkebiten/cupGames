import sched
import time
from .models import Account, Game, Category, Statistic, Comment, Score, Suggestion, Badge, Favorite, FavCategory, \
    OwnedBadges


def playLimitUpdate():
    accounts = Account.objects.all()
    for account in accounts:
        if account.type == "FU":
            account.playLimit = "2"
            account.save()
        elif account.type == "PU":
            account.playLimit = "10"
            account.save()
        else:
            account.playLimit = "100"
            account.save()
