from rest_framework.views import APIView
from tmm.apps.core.models import Translations
from tmm.apps.core.api.serializer import TranslationsSerializer
from rest_framework.response import Response


class TranslationsView(APIView):
    # GET /translations/?lang=en
    serializer_class = TranslationsSerializer

    def get_queryset(self):
        translations = Translations.objects.all()
        return translations

    def get(self, request, *args, **kwargs):
        i18nextArray = []
        try:
            lang = request.query_params["lang"]
            print(lang)
            translations_raw = Translations.objects.language(lang).all()

            for translation in translations_raw:
                i18nextArray.append({translation.key: translation.value})
        except:
            print("ERROR")

        return Response(i18nextArray)
        # lang = self.get_queryset()
        # serializer = TranslationsSerializer(lang, many=True)
