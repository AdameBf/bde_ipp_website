from django.db import models


class Member(models.Model):
    PROGRAMME_TYPES = (
        ('m1', 'Master 1'),
        ('m2', 'Master 2'),
        ('phd', 'PhD track'),
    )

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    programme_type = models.CharField(max_length=3, choices=PROGRAMME_TYPES)
    programme_name = models.CharField(max_length=63)
    membership_fee_paid = models.BooleanField(default=False)