from django.contrib import admin
from django.urls import path, include
from App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('App/', include('App.urls')),
]
