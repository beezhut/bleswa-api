from django.db import models
import uuid
from datetime import date

class Customer(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Customers"


class WareHouse(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, null=False)
    address = models.TextField(max_length=500, null=True, blank=True)
    longitude = models.CharField(max_length=10, null=True)
    latitude = models.CharField(max_length=10, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Warehouses"


class Asset(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    type = models.CharField(max_length=100, null=False)
    value = models.DecimalField(max_digits=15, decimal_places=2)
    warehouse = models.ForeignKey(WareHouse, null=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Assets"


class Branch(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name = models.CharField(max_length=100, null=False)
    ifsc = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Branches"


class Loan(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False) 
    loan_account_number = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=10, null=False)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    loan_created_date = models.DateField(default=date.today)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, null=True, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.loan_account_number)

    class Meta:
        verbose_name_plural = "Loans"