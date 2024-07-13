from django.contrib import admin
from django.urls import path
from restaurant_search import views

urlpatterns = [
    path('admin/', admin.site.urls),
]
