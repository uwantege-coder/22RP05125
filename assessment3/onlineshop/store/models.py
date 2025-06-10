from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def _str_(self):
        return self.name