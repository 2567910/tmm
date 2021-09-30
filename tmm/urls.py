
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
from rest_framework.views import APIView


# TODO: https://www.django-rest-framework.org/api-guide/routers/#drf-nested-routers

class TranslationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translations
        # fields = "__all__"
        fields = ('key')


class TranslationsView(viewsets.ModelViewSet):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer


    def list(self, request, *args, **kwargs):
        try:
            lang = request.query_params["lang"]
            print(lang)
        except:
            translations_raw = Translations.objects.language('de').all()
            i18nextArray = []
            for translation in translations_raw:
                i18nextArray.append({translation.key: translation.value})
        return Response(i18nextArray)


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'translations', TranslationsView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('/admin', admin.site.urls),
    path('admin/',    admin.site.urls),
    path('admin/<str:lang>', TranslationsView),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('', admin.site.urls),

# ]
# path('api-auth/', include('rest_framework.urls'))