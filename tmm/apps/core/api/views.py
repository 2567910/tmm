from rest_framework.views import APIView
from tmm.apps.translation_management_tool.models import Translation
from tmm.apps.core.api.serializer import TranslationsSerializer
from rest_framework.response import Response

import json

class TranslationsView(APIView):
    # GET /translations/project/lang
    serializer_class = TranslationsSerializer

    def get_queryset(self):
        translations = Translation.objects.all()
        return translations



    def get(self, request, *args, **kwargs):
        def get_full_key(obj):
            if (obj.key.get_ancestors()):
                return ".".join([lang.key for lang in obj.key.get_ancestors()]) + "." + obj.key.key
            else:
                return obj.key.key

        i18nextDict = {}
        try:
            lang = self.kwargs.get("lang")
            project = self.kwargs.get("project")
            translations_raw = Translation.objects.all()

            for translation in translations_raw:
                if translation.key.project.name == project and translation.language.code == lang:
                    i18nextDict.update({get_full_key(translation): translation.value})

            return Response(i18nextDict)
        except:
            print("ERROR")
            return Response({"error": "No translations found"})
