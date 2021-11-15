from django.db import models


class Member(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=256)
    birth_date = models.DateField()