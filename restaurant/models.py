from django.db import models

class Menu_Categories(models.Model):
    category_name = models.CharField(max_length = 30)
    restaurant = models.ManyToManyField(Restaurant)
    pass
    
    
