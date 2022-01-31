from django.conf.urls import url
from tmm.apps.translation_management_tool.api.views import TranslationsView

urlpatterns = [
    url(r'^(?P<project>\w+)/(?P<lang>[\w-]+)/$', TranslationsView.as_view()),
]