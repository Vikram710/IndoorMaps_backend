from django.db import models

class Dist(models.Model):
    rp = models.IntegerField()
    uid = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    enters = models.DateTimeField()
    exits = models.DateTimeField()