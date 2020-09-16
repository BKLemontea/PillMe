from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from . import models
from threading import Timer
import os

# Create your views here.
class PillDetailView(DetailView):
    
    model = models.Pill
    template_name='pills/detail.html'
    object_name = "pill"
    
def camera(request):
    def delete():
        try:
            pill.refresh_from_db()
            if pill.user == None:
                url = '.' + pill.file.url
                os.remove(url)
                pill.delete()
            pass
        except models.Pill.DoesNotExist:
            pass   
    
    file = request.FILES.get("camera")
    
    name = "약 이름"
    cycle = 1
    dosage = 1
    usage = "복용법"
    
    pill = models.Pill.objects.create(
        file = file,
        name = name,
        cycle = cycle,
        dosage = dosage,
        usage = usage,
    )
    
    Timer(3600, delete).start()
    
    return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))

@login_required
def add_inventory(request, pk):
    print("인벤토리 추가")
    try:
        pill = models.Pill.objects.get(pk=pk)
        pill.user = request.user
        pill.save()
        return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))
    except models.Pill.DoesNotExist:
        return redirect(reverse("core:home"))

@login_required
def delete_inventory(request, pk): 
    try:
        pill = models.Pill.objects.get(pk=pk)
        pill.delete()
        return redirect(reverse("core:home"))
    except models.Pill.DoesNotExist:
        return redirect(reverse("core:home"))
    