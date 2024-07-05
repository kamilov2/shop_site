from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

COLOUR =(
    ('grey','GREY'),
    ('black','BLACK'),
    ('red','RED'),
    ('blue','BLUE'),
    ('orange','ORANGE'),
    ('white','WHITE'),
)


class Product(models.Model):
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250,blank=True)
    colour = models.CharField(max_length=50,blank=True,choices=COLOUR)
    description = models.TextField()
    img = models.ImageField(upload_to='img/')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.IntegerField()
    
    def __str__(self):
        return self.title