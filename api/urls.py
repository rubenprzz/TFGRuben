from django.urls import path, include
from . import views
from .views import EstudianteView



urlpatterns = [
    path('estudiantes', EstudianteView.as_view()),
    path('', include('frontend.urls'))
]
