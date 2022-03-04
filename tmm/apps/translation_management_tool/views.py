from django.shortcuts import render
from django.conf.urls import url
from django.contrib import admin


def my_view(request):
    return render(request, 'admin/preferences/preferences.html')