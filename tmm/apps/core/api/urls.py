from django.conf.urls import url
from tmm.apps.core.api.views import TranslationsView

urlpatterns = [
    url(r'^(?P<project>\w+)/(?P<lang>[\w-]+)/$', TranslationsView.as_view()),
]