from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated
    
    def handle_no_permission(self):
        messages.error(self.request, "이미 로그인 중입니다.")
        return redirect("core:home")
    
class LoggedInOnlyView(LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_authenticated
    
    def handle_no_permission(self):
        messages.error(self.request, "로그인이 필요한\n서비스입니다.")
        return redirect("users:login")