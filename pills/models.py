from django.db import models
from core import models as core_models

# Create your models here.
class Pill(core_models.TimeStampedModel):
    file = models.ImageField(upload_to="pill_photos", blank=True, null=True)
    name = models.CharField(max_length=50)
    cycle = models.IntegerField(blank=True, null=True)
    dosage = models.IntegerField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    user = models.ForeignKey("users.User", related_name="pills", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name