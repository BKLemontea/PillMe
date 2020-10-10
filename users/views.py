from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, FormView, TemplateView
from django.contrib import messages
from pills import models as pill_models
from . import models, forms

# Create your views here.
class LoginView(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None :
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Welcome " + self.request.user.name)
        return reverse("core:home")
    
def log_out(request):
    messages.success(request, "Good Bye " + request.user.name)
    logout(request)
    return redirect(reverse("core:home"))
        
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
    
class InventoryView(TemplateView):
    template_name = "users/Inventory.html"