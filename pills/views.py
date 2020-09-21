from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models
from urllib.request import urlretrieve, urlopen
from PIL import Image
import os

# Create your views here.
class PillDetailView(DetailView):
    
    model = models.Pill
    template_name='pills/detail.html'
    object_name = "pill"
    
def camera(request):
    img = request.POST.get("image")
    img = Image.open(urlopen(img))
    img.save("test.png")
    
    name = "징카민정40mg"
    
    try:
        pill = models.Pill.objects.get(name__icontains=name)
        messages.success(request, "알약 검색을 완료했습니다.")
        return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))
    except models.Pill.objects.DoesNotExist:
        messages.error(request, "알약을 찾지 못했습니다.")
        return redirect(reverse("core:home"))
    
def search(request):
    name = request.GET.get("name")
    mark = request.GET.get("mark")
    shape = request.GET.get("shape")
    color = request.GET.get("color")
        
    model = models.Pill.objects.all()
    if name:
        model = model.filter(name__icontains=name)
            
    if mark:
        model = model.filter(Q(mark_front__icontains=mark) | Q( mark_back__icontains=mark))
            
    if shape:
        model = model.filter(shape=shape)
            
    if color:
        model = model.filter(Q(color_front__icontains=color) | Q( color_back__icontains=color))
        
    paginator = Paginator(model, 6)
    page = request.GET.get('page')
    
    try:
        pills = paginator.page(page)
    except PageNotAnInteger:
        pills = paginator.page(1)
    except EmptyPage:
        pills = paginator.page(paginator.num_pages)
    
    result = model.count()
    previous_page_number = 0
    has_previous = False
    next_page_number = 0
    has_next = False
    
    if page is not None:
        if page is not '1':
            previous_page_number = int(page) - 1
            has_previous = True

    if paginator.num_pages > 1:
        if page is None or int(page) < paginator.num_pages:
            if page is None:
                next_page_number = 2
            else:
                next_page_number = int(page) + 1
            has_next = True
            
    page_range = paginator.page_range
    if len(list(page_range)) > 5:
        if page is None:
            page_range = range(1, 6)
        else:
            if int(page) - 2 < 1:
                page_range = range(1, 6)
            else:
                if int(page) + 2 > int(paginator.num_pages):
                    page_range = range(int(paginator.num_pages) - 4, int(paginator.num_pages) + 1)
                else:
                    page_range = range(int(page) - 2, int(page) + 3)
    
    has_first = False
    has_last = False
    
    if not 1 in page_range:
        has_first = True
    if not int(paginator.num_pages) in page_range:
        has_last = True
        
    if page is None:
        number = 1
    else:
        number = int(page)
        
    context = {
        'number':number,
        'has_first':has_first,
        'has_last':has_last,
        "result":result,
        "page_range":page_range,
        "has_previous":has_previous,
        "previous_page_number":previous_page_number,
        "has_next":has_next,
        "next_page_number":next_page_number,
        'paginator':paginator,
        'pills': pills
    }
    return render(request, "pills/search.html", context)