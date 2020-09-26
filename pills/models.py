from django.db import models

# Create your models here.
class Pill(models.Model):
    image = models.ImageField(upload_to="pill_photos", blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    serial_number = models.IntegerField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_serial_number = models.IntegerField(blank=True, null=True)
    sortation = models.CharField(max_length=50, blank=True, null=True)
    nature = models.CharField(max_length=1024, blank=True, null=True)
    
    mark_front = models.CharField(max_length=50, blank=True, null=True)
    mark_back = models.CharField(max_length=50, blank=True, null=True)
    shape = models.CharField(max_length=10, blank=True, null=True)
    color_front = models.CharField(max_length=10, blank=True, null=True)
    color_back = models.CharField(max_length=10, blank=True, null=True)
    line_front = models.CharField(max_length=10, blank=True, null=True)
    line_back = models.CharField(max_length=10, blank=True, null=True)
    
    major_axis = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    minor_axis = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    thickness = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    material = models.TextField(null=True, blank=True)
    efficacy = models.TextField(null=True, blank=True)
    voulme = models.TextField(null=True, blank=True)
    caution = models.TextField(null=True, blank=True)
    etc = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name