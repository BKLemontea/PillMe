from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from core import mixins
from pills import models as pill_models
from . import models

# Create your views here.
class AddScheduleView(DetailView):
    
    model = pill_models.Pill
    template_name= "schedules/add_schedule.html"
    object_name = "pill"

@login_required
def add_schedule(request, pk):
    dow = request.POST.getlist("checkbox")
    date = request.POST.get("date")
    date = date.split(" ")
    
    hour = int(date[1])
    if date[0] == "오후":
        hour += 12
    if hour == 12:
        hour = 0
    minute = int(date[2])
    time = str(hour) + ":" + str(minute)
    schedule = models.Schedule.objects.create(
        date=time,
        pill=pill_models.Pill.objects.get(pk=pk),
        user=request.user
    )
    for day in dow:
        d = models.DayOfWeek.objects.get(name=day)
        schedule.dow.add(d)
    schedule.save()
    messages.success(request, "일정을 추가했습니다.")
    return redirect(reverse("schedules:list"))

def schedule_list(request):
    if not request.user.is_authenticated:
        messages.error(request, "로그인이 필요한\n서비스입니다.")
        return redirect(reverse("users:login"))
    model = request.user.schedules.all()
        
    paginator = Paginator(model, 6)
    page = request.GET.get('page')
    
    try:
        schedules = paginator.page(page)
    except PageNotAnInteger:
        schedules = paginator.page(1)
    except EmptyPage:
        schedules = paginator.page(paginator.num_pages)
    
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
        'schedules': schedules
    }
    return render(request, "schedules/schedule_list.html", context)