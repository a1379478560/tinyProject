from django.db import models

# Create your models here.
class Investors(models.Model):
    investor_id=models.IntegerField(null=False,primary_key=True)
    name=models.CharField(null=False,max_length=64)
    ssn=models.CharField(null=True,unique=True,max_length=12)
    address=models.CharField(null=True,max_length=500,)

class stocks(models.Model):
    ticker=models.CharField(null=False,max_length=10,primary_key=True)
    company=models.CharField(null=False,max_length=500,)
    stock_class=models.CharField(max_length=100,null=False)

class portfolio(models.Model):
    trade_id=models.IntegerField(null=False,primary_key=True,auto_created=True)
    investor_id=models.ForeignKey("Investors",on_delete=models.DO_NOTHING,null=False)
    ticker=models.ForeignKey("stocks",on_delete=models.DO_NOTHING,null=False)
    price=models.IntegerField(null=False,)
    num=models.IntegerField(null=False)