from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home',views.home,name='home'),
    path('', auth_views.LoginView.as_view(template_name='timetable/login.html'), name='login'),
    path('register', views.register_request, name='register'),

]
