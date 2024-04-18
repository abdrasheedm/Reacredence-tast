from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Bill(models.Model):
    items = models.ManyToManyField(Item, through='BillItem')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total_cost(self):
        total = sum(item.price for item in self.items.all())
        self.total_cost = total
        self.save()

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def get_subtotal(self):
        return self.item.price * self.quantity
