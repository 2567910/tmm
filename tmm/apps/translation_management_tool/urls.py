from django.conf.urls import url
from tmm.apps.translation_management_tool.views import translations_view

urlpatterns = [
    url(r'^(?P<project>\w+)/(?P<lang>[\w-]+)/$', translations_view, name='i18next_json'),
]