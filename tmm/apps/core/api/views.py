from rest_framework.views import APIView
from tmm.apps.core.models import Translations
from tmm.apps.core.api.serializer import TranslationsSerializer
from rest_framework.response import Response

import json

class TranslationsView(APIView):
    # GET /translations/?lang=en
    serializer_class = TranslationsSerializer

    def get_queryset(self):
        translations = Translations.objects.all()
        return translations

    def get(self, request, *args, **kwargs):
        i18nextDict = {}
        try:
            lang = request.query_params["lang"]
            print(lang)
            translations_raw = Translations.objects.language(lang).all()

            for translation in translations_raw:
                i18nextDict.update({translation.key: translation.value})

            # finalJSON = json.dumps(i18nextDict)

            return Response(i18nextDict)
        except:
            print("ERROR")
            return Response(i18nextDict)


        # lang = self.get_queryset()
        # serializer = TranslationsSerializer(lang, many=True)
