from tmm.apps.translation_management_tool.models import Translation
from rest_framework import routers, serializers, viewsets


class TranslationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translation
        # fields = "__all__"
        fields = (['key'])