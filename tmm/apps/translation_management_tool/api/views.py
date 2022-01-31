from rest_framework.views import APIView
from tmm.apps.translation_management_tool.models import Translation
from tmm.apps.translation_management_tool.api.serializer import TranslationsSerializer
from rest_framework.response import Response


def get_keys(obj):
    arr = []
    if (obj.key.get_ancestors()):
        for an in obj.key.get_ancestors():
            arr.append(an.key)
        arr.append(obj.key.key)
        return arr
    else:
        arr.append(obj.key.key)
        return arr


def set_value_in_dict_recursive(i18nextDict, keysArray, value):
    if (len(keysArray) == 1):
        i18nextDict[keysArray[0]] = value
    else:
        if (type(i18nextDict[keysArray[0]]) is not dict):
            i18nextDict[keysArray[0]] = dict()
        set_value_in_dict_recursive(
            i18nextDict[keysArray[0]], keysArray[1:], value)
    return i18nextDict


class TranslationsView(APIView):
    # GET /translations/project/lang
    serializer_class = TranslationsSerializer

    def get_queryset(self):
        translations = Translation.objects.all()
        return translations

    def get(self, request, *args, **kwargs):

        try:
            lang = self.kwargs.get("lang")
            project = self.kwargs.get("project")

            translations_raw = Translation.objects.all().filter(
                language__code=lang, key__project__name=project)
            translation_list = list(translations_raw)

            translations_sortet_by_depth = sorted(
                translation_list, key=lambda d: d.key.get_depth())

            i18nextDict = dict()

            for translation in translations_sortet_by_depth:
                keys = get_keys(translation)

                i18nextDict = set_value_in_dict_recursive(
                    i18nextDict, keys, translation.value)
                print(i18nextDict)

            return Response(i18nextDict)

        except:
            print("ERROR")
            return Response({"error": "No translations found"})