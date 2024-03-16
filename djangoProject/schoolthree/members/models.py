from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone_no = models.IntegerField(null=True)
    created_at = models.DateField(null=True)