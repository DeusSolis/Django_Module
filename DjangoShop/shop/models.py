from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    wallet = models.IntegerField(default=10000)

    def __str__(self):
        return self.username


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    price = models.PositiveIntegerField(default=0)
    quantity_in_stock = models.PositiveIntegerField(default=1)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'id_{self.id} | {self.name}'


class Purchase(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_of_products = models.PositiveIntegerField(default=1)
    time_of_buy = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Purchase from {self.user} | Goods - {self.product.name} | Quantity {self.quantity_of_products} '


class PurchaseReturns(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    time_of_request = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Return from {self.purchase.user} | Good {self.purchase.product.name}  | Quantity {self.purchase.quantity_of_products} '
