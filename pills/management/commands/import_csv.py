from django.core.management.base import BaseCommand
from pills import models
import csv
import os
from urllib.request import urlretrieve

class Command(BaseCommand):
    
    help = "Importing csv file"
        
    def handle(self, *args, **options):
        data = open('./static/data/data.csv','rt',encoding='UTF8').readlines() 
        path = os.path.join("./media/pill_photos/")
        
        if not os.path.isdir(path):
            os.mkdir(path)
            
        for i in range(1, 2):
            d = data[i].split(",")
            date = list(d[28])
            date.insert(4, '-')
            date.insert(7, '-')
            date = ''.join(date)
            try:
                pill = models.Pill.objects.get(serial_number=d[0])
                pill.name = d[1]
                pill.serial_number = d[0]
                pill.company_name = d[3]
                pill.company_serial_number = d[2]
                pill.sortation = d[19]
                pill.nature = d[4]
                pill.mark_front = d[6]
                pill.mark_back = d[7]
                pill.shape = d[8]
                pill.color_front = d[9]
                pill.color_back = d[10]
                pill.line_front = d[11]
                pill.line_back = d[12]
                pill.major_axis = d[13]
                pill.minor_axis = d[14]
                pill.thickness = d[15]
                pill.date = date
            except models.Pill.DoesNotExist:
                pill = models.Pill.objects.create(
                    name = d[1],
                    serial_number = d[0],
                    company_name = d[3],
                    company_serial_number = d[2],
                    sortation = d[19],
                    nature = d[4],
                    mark_front = d[6],
                    mark_back = d[7],
                    shape = d[8],
                    color_front = d[9],
                    color_back = d[10],
                    line_front = d[11],
                    line_back = d[12],
                    major_axis = d[13],
                    minor_axis = d[14],
                    thickness = d[15],
                    date = date,
                )
            filename = str(pill.pk) + ".jpg"
            urlretrieve(d[5], "./media/pill_photos/" + filename)
            pill.image = "pill_photos/" + filename
            pill.save()
            
        self.stdout.write(self.style.SUCCESS("Complete"))