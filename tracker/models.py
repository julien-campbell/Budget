from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class  transaction(models.Model):
    expense = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=False)
    comment = models.TextField()
    transactor = models.ForeignKey(User, on_delete = models.CASCADE, default= None)