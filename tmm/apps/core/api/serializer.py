from tmm.apps.core.models import Translations
from rest_framework import routers, serializers, viewsets


class TranslationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translations
        # fields = "__all__"
        fields = (['key'])
