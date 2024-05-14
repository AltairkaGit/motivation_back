from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Quote(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField()
    author = models.TextField(default='')

    def __str__(self):
        return self.text