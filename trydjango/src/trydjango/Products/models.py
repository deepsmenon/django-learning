from django.db import models

# Create your models here.
class Products(models.Model):
  title = models.CharField(max_length= 120) #max_length = required
  Discription = models.TextField(blank = True, null = True)
  price = models. DecimalField(decimal_places=2, max_digits= 10000)
  Summurry = models.TextField()
  featured = models.BooleanField(default=True)