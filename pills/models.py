from django.db import models

# Create your models here.
class Pill(models.Model):
    file = models.ImageField(upload_to="pill_photos", blank=True, null=True)
    name = models.CharField(max_length=50)
    cycle = models.IntegerField(blank=True, null=True)
    dosage = models.IntegerField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name