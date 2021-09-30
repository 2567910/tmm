
from django.urls import path, include
from django.contrib.auth.models import User
from django.core import serializers
from rest_framework import routers, serializers, viewsets
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from tmm.apps.core.models import Translations
from rest_framework.response import Response
from django.contrib import admin
from rest_framework.routers import Route, DynamicRoute, SimpleRouter
from rest_framework import generics



from tmm.apps.core.api.views import TranslationsView


# TODO: https://www.django-rest-framework.org/api-guide/routers/#drf-nested-routers



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# router.register(r'translations', TranslationsView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    # path('/admin', admin.site.urls),
    path('admin/',    admin.site.urls),
    path('translations/',    include('tmm.apps.core.api.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('', admin.site.urls),

# ]
# path('api-auth/', include('rest_framework.urls'))