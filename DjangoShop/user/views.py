from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import CreateView

from .forms import UserForm
from .models import MyUser


class Login(LoginView):
    template_name = 'login.html'
    success_url = '/'


class Logout(LogoutView):
    next_page = '/'


class UserCreateView(CreateView):
    model = MyUser
    form_class = UserForm
    success_url = '/login/'
    template_name = 'registration.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(self.object.password)
        self.object.save()
        return super().form_valid(form)

