# questions/views/auth.py

from django.views.generic import FormView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.shortcuts import redirect
from questions.forms.auth import RegistrationForm, LoginForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class RegisterView(FormView):
    template_name = "auth/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("questions:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class LoginView(BaseLoginView):
    template_name = "auth/login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("questions:home")


@login_required
def logout_view(request):
    logout(request)
    return redirect("questions:login")