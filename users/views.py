from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib import messages
from pills import models as pill_models
from . import models

# Create your views here.
@login_required
def add_inventory(request, pk):
    pass
    try:
        pill = pill_models.Pill.objects.get(pk=pk)
        user = request.user
        user.inventory.add(pill)
        user.save()
        messages.success(request, "인벤토리에 추가했습니다.")
        return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))
    except pill_models.Pill.DoesNotExist:
        messages.error(request, "에러가 발생습니다.")
        return redirect(reverse("core:home"))

@login_required
def delete_inventory(request, pk): 
    pass
    try:
        pill = pill_models.Pill.objects.get(pk=pk)
        user = request.user
        user.inventory.remove(pill)
        user.save()
        messages.success(request, "인벤토리에서 삭제했습니다.")
        return redirect(reverse("pills:detail", kwargs={'pk':pill.pk}))
    except models.Inventory.DoesNotExist:
        messages.success(request, "인벤토리에서 해당 알약을 찾지 못했습니다.")
        return redirect(reverse("core:home"))