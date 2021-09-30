from django.conf.urls import url
from tmm.apps.core.api.views import TranslationsView

urlpatterns = [
    url('', TranslationsView.as_view()),
]