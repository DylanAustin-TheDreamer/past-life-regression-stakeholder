from django.contrib import admin
from django.urls import path

from PastLife import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
]