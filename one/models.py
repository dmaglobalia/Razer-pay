from django.db import models

# Create your models here.

class pay(models.Model):
    payment = models.IntegerField()

    def __str__(self):
        return str(self.payment)