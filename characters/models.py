from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=20)
    characteristic = models.TextField()
    image = models.ImageField(upload_to='characters')
    turn_order = models.IntegerField()
    character_priority = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return self.name