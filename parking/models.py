from django.db import models

class Park(models.Model):
    uid = models.IntegerField()
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    status = models.CharField(max_length=30)