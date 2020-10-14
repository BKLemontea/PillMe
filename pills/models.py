from django.db import models

# Create your models here.
class Pill(models.Model):
    image = models.ImageField(upload_to="pill_photos", blank=True, null=True) # 알약 사진
    name = models.CharField(max_length=100, blank=True, null=True) # 제품명
    serial_number = models.IntegerField(blank=True, null=True) # 제품 일련번호
    company_name = models.CharField(max_length=100, blank=True, null=True) # 제조사
    company_serial_number = models.IntegerField(blank=True, null=True) # 제조사 일련번호
    sortation = models.CharField(max_length=50, blank=True, null=True) # 전문/일반
    nature = models.CharField(max_length=1024, blank=True, null=True) # 성상
    
    mark_front = models.CharField(max_length=50, blank=True, null=True) # 문자 앞
    mark_back = models.CharField(max_length=50, blank=True, null=True) # 문자 뒤
    shape = models.CharField(max_length=10, blank=True, null=True) # 모양
    color_front = models.CharField(max_length=10, blank=True, null=True) # 색상 앞
    color_back = models.CharField(max_length=10, blank=True, null=True) # 색상 뒤
    line_front = models.CharField(max_length=10, blank=True, null=True) # 분할선 앞
    line_back = models.CharField(max_length=10, blank=True, null=True) # 분할선 뒤
    
    major_axis = models.CharField(max_length=10, blank=True, null=True) # 장축
    minor_axis = models.CharField(max_length=10, blank=True, null=True) # 단축
    thickness = models.CharField(max_length=10, blank=True, null=True) # 두께
    
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    
    permission_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True) # 허가일
    cancel = models.CharField(max_length=50, blank=True, null=True) # 취소/취하
    cancel_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True) # 취소/취하일자
    
    material = models.TextField(null=True, blank=True) # 원료
    efficacy = models.TextField(null=True, blank=True) # 효능효과
    voulme = models.TextField(null=True, blank=True) # 용법
    caution = models.TextField(null=True, blank=True) # 주의사항
    dur = models.TextField(null=True, blank=True) # DUR
    etc = models.TextField(null=True, blank=True) # 기타
    unit = models.CharField(max_length=50, blank=True, null=True) # 단위
    production_performance = models.TextField(null=True, blank=True) # 생산실적
    history = models.TextField(null=True, blank=True) # 변경이력
    
    def __str__(self):
        return self.name