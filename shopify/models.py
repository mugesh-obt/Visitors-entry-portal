from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)

    class Meta:
        db_table = "data"


