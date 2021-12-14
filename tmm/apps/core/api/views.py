from rest_framework.views import APIView
from tmm.apps.translation_management_tool.models import Translation
from tmm.apps.core.api.serializer import TranslationsSerializer
from rest_framework.response import Response

import json

class TranslationsView(APIView):
    # GET /translations/?lang=en
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

            print(lang)
            translations_raw = Translation.objects.all()
            print(translations_raw)


            for translation in translations_raw:
                if translation.key.project.name == project:
                    if translation.language.code == lang:
                        i18nextDict.update({get_full_key(translation): translation.value})
                        # i18nextDict[translation.key.key] = translation.value
            print(i18nextDict)

            # finalJSON = json.dumps(i18nextDict)

            # if (obj.key.get_ancestors()):
            #     return ".".join([lang.key for lang in obj.key.get_ancestors()]) + "." + obj.key.key
            # else:
            #     return obj.key.key


            return Response(i18nextDict)
        except:
            print("ERROR")
            return Response(i18nextDict)


        # lang = self.get_queryset()
        # serializer = TranslationsSerializer(lang, many=True)
