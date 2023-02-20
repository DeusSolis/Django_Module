from django.urls import path
from .views import UserCreateView, Login, Logout

urlpatterns = [
    path('registration/', UserCreateView.as_view(), name='registration'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]