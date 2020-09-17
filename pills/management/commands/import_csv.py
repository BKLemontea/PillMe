from django.core.management.base import BaseCommand
from pills import models
import csv
import os
from urllib.request import urlretrieve

class Command(BaseCommand):
    
    help = "Importing csv file"
    
    def add_arguments(self, parser):
        data = open('./static/data/data.csv','rt',encoding='UTF8').readlines()
        parser.add_argument(
            "--number", default=len(data), type=int, help = "How many pills do you want to create"
        )
        parser.add_argument(
            "--data", type=list, default=data
        )
        
    def handle(self, *args, **options):
        data = options.get("data")
        number = options.get("number")
        path = os.path.join("./media/pill_photos/")
        
        if not os.path.isdir(path):
            os.mkdir(path)
            
        for i in range(1, number+1):
            print(i, "회 Importing...")
            d = data[i].split(",")
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
                )
            filename = str(pill.pk) + ".jpg"
            urlretrieve(d[5], "./media/pill_photos/" + filename)
            pill.image = "pill_photos/" + filename
            
            if list(d[13])[0] != "-":
                pill.major_axis = d[13]
                
            if list(d[14])[0] != "-":
                pill.minor_axis = d[14]
                
            if list(d[15])[0] != "-":
                pill.thickness = d[15]
            
            date = list(d[28])
            if date[0] != '-':
                date.insert(4, '-')
                date.insert(7, '-')
                date = date[:10]
                pill.date = ''.join(date)
            pill.save()
            
        self.stdout.write(self.style.SUCCESS("Complete"))