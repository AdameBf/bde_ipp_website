from django.db import models


class Member(models.Model):
    MASTER_LEVELS = (
        ('m1', 'Master 1'),
        ('m2', 'Master 2'),
    )

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    master_level = models.CharField(max_length=2, choices=MASTER_LEVELS)
    phd_track = models.BooleanField(default=False)
    programme_name = models.CharField(max_length=63)
    membership_fee_paid = models.BooleanField(default=False)
