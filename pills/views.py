from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from . import models
from threading import Timer
import os

# Create your views here.
class PillDetailView(DetailView):
    
    model = models.Pill
    template_name='pills/detail.html'
    object_name = "pill"
    
def camera(request):
    file = request.FILES.get("camera")
    
    name = "약 이름"
    cycle = 1
    dosage = 1
    usage = "복용법"
    
    try:
        pill = models.Pill.objects.get(name=name)
        messages.success(request, "알약 검색을 완료했습니다.")
        return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))
    except models.Pill.objects.DoesNotExist:
        messages.error(request, "알약을 찾지 못했습니다.")
        return redirect(reverse("core:home"))
    
    