from django.db import models

# Create your models here.

class Restaurant(models.Model):
	restaurant_name = models.CharField(max_length=30)
	restaurant_location = models.CharField(max_length=30)
	restaurant_menu = models.CharField(max_length=30)
	pass
class Menu_Categories(models.Model):
    category_name = models.CharField(max_length = 30)
    restaurant = models.ManyToManyField(Restaurant)
    pass
class Menu_Items(models.Model):
	item_name = models.CharField(max_length=30)
	menu_categories = medels.ManyToManyField(Menu_Categories)
