from django.db import models
from core import models as core_models

# Create your models here.
class Log(core_models.TimeStampedModel):
    name = models.CharField(max_length=50)
    dosage = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey("users.User", related_name="logs", on_delete=models.CASCADE)