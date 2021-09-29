
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from tmm.apps.core.models import Translations
from django.contrib import admin
from rest_framework.routers import Route, DynamicRoute, SimpleRouter

# TODO: https://www.django-rest-framework.org/api-guide/routers/#drf-nested-routers

class TranslationsSerializer(TranslatableModelSerializer):
    i18nextStructure = {
        "text": "Dieser Text ist Deutschw"
    }
    translations = TranslatedFieldsField(shared_model=Translations)
    # translations.objects.all()
    print(translations)
    # for translation in translations():
        # print(translation)


    class Meta:
        model = Translations
        fields = ('id', 'key', 'translations')


class TranslationsViewSet(viewsets.ModelViewSet):
    queryset = Translations.objects.all()
    serializer_class = TranslationsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'translations', TranslationsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('/admin', admin.site.urls),
    path('admin/',    admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

# urlpatterns = [
#     path('', admin.site.urls),

# ]
# path('api-auth/', include('rest_framework.urls'))