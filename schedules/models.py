from django.db import models

# Create your models here.
class Schedule(models.Model):
    date = models.TimeField()
    dow = models.ManyToManyField("schedules.DayOfWeek", related_name="dayofweek")
    pill = models.ForeignKey("pills.Pill", related_name="schedules", on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", related_name="schedules", on_delete=models.CASCADE)
    
class DayOfWeek(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
    def first(self):
        return self.name[0]