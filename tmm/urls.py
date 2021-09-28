
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from tmm.apps.core.models import Test
from django.contrib import admin


class TranslationsSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Test)

    class Meta:
        model = Test
        fields = ('id', 'translations')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TranslationsViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TranslationsSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
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