from django.urls import path
from . import views
from .views import EstudianteView



urlpatterns = [
    path('', views.home, name='home'),
    path('estudiantes', EstudianteView.as_view()),
]
