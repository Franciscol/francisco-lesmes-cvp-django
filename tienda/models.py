from django.db import models

# Create your models here.

class Producto(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    

class Venta(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    date_sold = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.product.quantity -= self.quantity_sold
        self.product.save()
        super().save(*args, **kwargs)
