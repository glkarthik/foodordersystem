from uuid import uuid4

from django.db import models


# Create your models here.
class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, null=False, db_index=True, unique=True, editable=False, default=uuid4)
    title = models.CharField(max_length=200)
    unit_price = models.DecimalField(decimal_places=2, max_digits=60)
    qty = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.title + " " + str(self.id)
