from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from transactions import views as transactions_views


urlpatterns = [
    path('', transactions_views.home, name='home'),
]
