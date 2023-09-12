from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField()
    power = models.IntegerField(default=0)
    mana = models.IntegerField(default=0)
    categories = models.CharField(max_length=255, default="Item")