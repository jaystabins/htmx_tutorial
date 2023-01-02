from django.db import models
import uuid
from django.urls import reverse


class Item(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name   

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})
    
