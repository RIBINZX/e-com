from django.db import models

# Create your models here.

class Categories(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = 'Categories'
        ordering = ['name']
    

class Subcategories(models.Model):
    category=models.ForeignKey(Categories, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Subcategories"
        verbose_name_plural = 'Subcategories'
        ordering = ['name']


class Product(models.Model):
    subcategory=models.ForeignKey(Subcategories, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='products')
    price=models.IntegerField()
    description=models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = 'Products'
        ordering = ['name']