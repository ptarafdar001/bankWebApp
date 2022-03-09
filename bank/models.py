from django.db import models

# Create your models here.
class Accounts(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    accountNo = models.IntegerField()
    balance = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)


class Transactions(models.Model):
    fromAcc = models.CharField(max_length=100)
    toAcc = models.CharField(max_length=100)
    balance = models.IntegerField()
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True)
