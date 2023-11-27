from django.urls import path

from .views import Login, register,log,ProfileView

urlpatterns = [
    path('login/', Login, name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', register, name='register'),
    path('logout/', log, name='logout'),
]
