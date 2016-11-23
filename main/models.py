from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(verbose_name='ЧПУ категории')
    
    def __str__(self):
        return '{}'.format(self.title)
    
class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(verbose_name='ЧПУ товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(Category)
    photo = models.ImageField(upload_to='media/', blank=True)
    
    def __str__(self):
        return '{}'.format(self.title)