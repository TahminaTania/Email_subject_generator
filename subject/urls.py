from django.urls import path
from . import views

urlpatterns = [
    path('', views.mail, name='home'),
    path('registation/', views.registerPage, name="reg"),
    path('old_user/', views.loginPage, name="log"),
]
