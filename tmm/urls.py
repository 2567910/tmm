
from django.urls import path, include
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib import admin

urlpatterns = [
    # path('/admin', admin.site.urls),
    path('admin/',    admin.site.urls),
    path('translations/',    include('tmm.apps.translation_management_tool.urls')),
]
