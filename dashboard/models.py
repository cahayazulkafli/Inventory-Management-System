from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
	('Food', 'Food'),
	('Drinks', 'Drinks'),
	('Cooking Utensil', 'Cooking Utensil'),
	('Personal Hygiene', 'Personal Hygiene'),
)

class Product(models.Model):
    name = models.CharField(max_length = 100, null = True)
    category = models.CharField(max_length = 20, choices = CATEGORY, null = True)
    quantity = models.PositiveIntegerField(null = True)
    
    def __str__(self):
        return f'{self.name} - {self.quantity}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    staff = models.ForeignKey(User, models.CASCADE, null = True)
    orderquantity = models.PositiveIntegerField(null = True)
    date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f'{self.product} has been ordered by {self.staff.username}'