from django.db import models

# Create your models here.
class Schedule(models.Model):
    date = models.DateTimeField()
    dosage = models.IntegerField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    pill = models.ForeignKey("pills.Pill", related_name="schedules", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="schedules", on_delete=models.CASCADE)