from django.db import models
from django.db.models import JSONField

class dish_search(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    items = JSONField()
    cordinates = models.CharField(max_length=50)
    detailDump = JSONField()

    def __str__(self):
        return self.name
