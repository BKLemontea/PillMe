from django.core.management.base import BaseCommand
from pills import models
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import csv, os, requests, re

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
            
            drug_info = parshing(d[0])
            
            name = remove(d[1])
            mark_front = remove_mark(d[6])
            mark_back = remove_mark(d[7])
            
            try:
                pill = models.Pill.objects.get(serial_number=d[0])
                pill.name = name
                pill.serial_number = d[0]
                pill.company_name = d[3]
                pill.company_serial_number = d[2]
                pill.sortation = d[19]
                pill.nature = d[4]
                pill.mark_front = mark_front
                pill.mark_back = mark_back
                pill.shape = d[8]
                pill.color_front = d[9]
                pill.color_back = d[10]
                pill.line_front = d[11]
                pill.line_back = d[12]
                pill.material = drug_info[1]
                pill.efficacy = drug_info[2]
                pill.voulme = drug_info[3]
                pill.caution = drug_info[4]
                pill.dur = drug_info[5]
                pill.etc = drug_info[6]
                pill.unit = drug_info[7][0]
                pill.production_performance = drug_info[7][1]
                pill.history = drug_info[8]

            except models.Pill.DoesNotExist:
                pill = models.Pill.objects.create(
                    name = name,
                    serial_number = d[0],
                    company_name = d[3],
                    company_serial_number = d[2],
                    sortation = d[19],
                    nature = d[4],
                    mark_front = mark_front,
                    mark_back = mark_back,
                    shape = d[8],
                    color_front = d[9],
                    color_back = d[10],
                    line_front = d[11],
                    line_back = d[12],
                    material = drug_info[1],
                    efficacy = drug_info[2],
                    voulme = drug_info[3],
                    caution = drug_info[4],
                    dur = drug_info[5],
                    etc = drug_info[6],
                    unit = drug_info[7][0],
                    production_performance = drug_info[7][1],
                    history = drug_info[8],
                )
            
            for base_info in drug_info[0]:
                if base_info[0] == "허가일":
                    pill.permission_date = base_info[1]
                elif base_info[0] == "취소/취하구분":
                    pill.cancel = base_info[1]
                elif base_info[0] == "취소/취하일자":
                    pill.cancel_date = base_info[1]
            
            if d[5] != '-':
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
        
def remove(name):
    name = list(name)

    cnt = 0
    flag = False
    while True:
        if name[cnt] == '(' or name[cnt] == '<':
            flag = True
            del name[cnt]
            cnt -= 1
        elif name[cnt] == ')' or name[cnt] == '>':
            flag = False
            del name[cnt]
            cnt -= 1
        elif flag:
                del name[cnt]
                cnt -= 1
        cnt += 1
        
        if cnt >= len(name):
            name = ''.join(name)
            break

    return name

def remove_mark(mark):
    mark = mark.replace("분할선", "")
    if mark == '':
        mark = '-'
    return mark

def parshing(ItemNumber):
    URL = f"https://nedrug.mfds.go.kr/pbp/CCBBB01/getItemDetail?itemSeq={ItemNumber}" 
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser") 
    
    drug_html_class = soup.find("div", {"class": "drug_container"})  # 약 정보
    
    drug_info = []
    drug_info.append(get_drug_base_info(drug_html_class.find("div", {"class": "r_sec"}))) # 기본정보
    drug_info.append(get_drug_material(drug_html_class.find("div", {"id": "scroll_02"}))) # 원료
    drug_info.append(get_drug_info(drug_html_class.find("div", {"id": "scroll_03"}))) # 효능
    drug_info.append(get_drug_info(drug_html_class.find("div", {"id": "scroll_04"}))) # 사용량,용법
    drug_info.append(get_drug_info(drug_html_class.find("div", {"id": "scroll_05"}))) # 주의사항
    drug_info.append(get_drug_etc(drug_html_class.find("div", {"id": "scroll_06"}))) # DUR
    drug_info.append(get_drug_etc(drug_html_class.find("div", {"id": "scroll_07"}))) # 기타정보
    drug_info.append(get_drug_pp(drug_html_class.find("div", {"id": "scroll_08"}))) # 생산실적
    drug_info.append(get_drug_etc(drug_html_class.find("div", {"id": "scroll_10"}))) # 변경이력

    return drug_info

def get_drug_base_info(html):
    try:
        temp = []
        tr_list = html.find_all("tr")

        for tr in tr_list:
            th = re.sub('<.+?>', '', str(tr.find("th")), 0).strip()
            td = re.sub('<.+?>', '', str(tr.find("td")), 0).strip()
            temp.append([th, td])
        return temp
    except:
        pass

def get_drug_material(html):
    try:
        temp = ''
        info_box_list = html.find_all("div", {"class": "info_box"})
        title4_list = html.find_all("h3", {"class": "cont_title4"})
        title5_list = html.find_all("h3", {"class": "cont_title5"})
        for cnt in range(len(info_box_list)):
            temp += str(info_box_list[cnt])
            try:
                temp += str(title4_list[cnt])
            except:
                pass
            try:
                temp += str(title5_list[cnt])
            except:
                pass
        temp = re.sub('<!--.+?-->', '', temp, 0).strip()
        return temp
    except:
        pass


def get_drug_info(html):
    try:
        temp = str(html.find("div", {"class": "info_box"}))
        temp = re.sub('<caption>.+?</caption>', '', temp, 0)
        temp = re.sub('<!--.+?-->', '', temp, 0).strip()
        return temp
    except:
        pass
    
def get_drug_etc(html):
    try:
        temp = str(html.find("table", {"class": "s-dr_table"}))
        temp = re.sub('<a.+?>', '', temp, 0)
        temp = re.sub('</a>', '', temp, 0)
        temp = re.sub('<caption>.+?</caption>', '', temp, 0)
        temp = re.sub('<!--.+?-->', '', temp, 0).strip()
        return temp
    except:
        pass
    
def get_drug_pp(html):
    try:
        unit = re.sub('<.+?>', '', str(html.find("span", {"class": "stt"})), 0).strip()
        pp = get_drug_etc(html)
        return [unit, pp]
    except:
        return [None, None]