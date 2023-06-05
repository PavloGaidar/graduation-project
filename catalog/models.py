from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    features = models.TextField()
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category' )
    

class Comment(models.Model):
    name = models.CharField(max_length=255)
    messages = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name='comments' )