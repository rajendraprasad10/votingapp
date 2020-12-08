from django.db import models
from django.contrib.auth.models import User

# create condidate model
class add_Candidates(models.Model):
    liked = models.ManyToManyField(User, default = None, blank = True)

@property
def con_votes(self):
    return self.liked.all().count()

LIKE_CHOICES = (
    ('Vote', 'Vote'),
    ('Not-Vote', 'Not-Vote')
)

# create a like model
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    con = models.ForeignKey(add_Candidates, on_delete=models.CASCADE)
    value = models.CharField(choices= LIKE_CHOICES,default='Vote',max_length=100)

    def __str__(self):
        return str(self.user)