from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    year = models.DateTimeField(blank=True, null=True)
    product_type = models.BooleanField(default=True)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
