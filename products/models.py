from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        # return name to display on site 
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    quantity_in_stock = models.IntegerField(blank=False)
    in_stock = models.BooleanField(default=False)
    animal_type = models.CharField(max_length=254, blank=True)


    def __str__(self):
        return self.name

    def get_stock_level(self):
        # get number in stock 
        return self.quantity_in_stock

    def change_to_out_of_stock(self):
        # automatically change stock label
        if self.quantity_in_stock < 1:
            self.in_stock = False
            self.save()
