from django.db import models
from vote.models import VoteModel
from django.conf import settings
from django.utils import timezone

class GhostPost(VoteModel, models.Model):
    body = models.CharField(max_length=280)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    boast = models.BooleanField()
    created_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        votes = self.likes - self.dislikes
        if self.boast:
            return "{} - {}".format(votes, "boast")
        else:
            return "{} - {}".format(votes, "roast")