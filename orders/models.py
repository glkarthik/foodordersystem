from uuid import uuid4

from django.db import models


# Create your models here.
class Order(models.Model):
    id = models.UUIDField(primary_key=True, null=False, db_index=True, unique=True, editable=False, default=uuid4)
    date = models.DateTimeField()
    items = models.ManyToManyField("inventories.Inventory", related_name='menu_items')
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return str(self.id)
