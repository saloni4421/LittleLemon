from django.db import models

class cat(models.Model):
    catname = models.CharField(max_length=100)

    def __str__(self):
        return self.catname

# Create your models here.
class MenuItem(models.Model):
    categories = models.ForeignKey(cat, on_delete= models.CASCADE)
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=200)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Image = models.ImageField(upload_to='menu_items/')

    def __str__(self):
        return self.Name