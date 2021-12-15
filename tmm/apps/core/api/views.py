from rest_framework.views import APIView
from tmm.apps.translation_management_tool.models import Translation
from tmm.apps.core.api.serializer import TranslationsSerializer
from rest_framework.response import Response

from addict import Dict
import operator

class TranslationsView(APIView):
    # GET /translations/project/lang
    serializer_class = TranslationsSerializer

    def get_queryset(self):
        translations = Translation.objects.all()
        return translations



    def get(self, request, *args, **kwargs):
        def get_keys(obj):
            arr = []
            print(arr)
            if (obj.key.get_ancestors()):
                for an in obj.key.get_ancestors():
                    arr.append(an.key)
                arr.append(obj.key.key)
                print(arr)
                return arr
            else:
                arr.append(obj.key.key)
                print(arr)
                return arr


        def set_value_in_dict_recursive(i18nextDict, keysArray, value):
            if (len(keysArray) == 1):
                i18nextDict[keysArray[0]] = value
            else:
                if (type(i18nextDict[keysArray[0]]) is not dict):
                    i18nextDict[keysArray[0]] = dict()
                i18nextDict[keysArray[0]] = set_value_in_dict_recursive(i18nextDict[keysArray[0]], keysArray[1:], value)
            return i18nextDict


        # def set_value_in_dict(numberOfAncestors, keysArray, value):

        #     print(numberOfAncestors, keysArray)
        #     if numberOfAncestors == 1:
        #         i18nextDict[keysArray[0]] = value
        #     elif numberOfAncestors == 2:
        #         print("IT Worked")
        #         if type(i18nextDict[keysArray[0]]) is not dict:
        #             i18nextDict[keysArray[0]] = {}

        #         i18nextDict[keysArray[0]][keysArray[1]] = value
        #     elif numberOfAncestors == 3:
        #         print("IT Worked")
        #         # i18nextDict[keysArray[0]][keysArray[1]][keysArray[2]] = value
        #         print("IT Worked2")
        #     elif numberOfAncestors == 4:
        #         i18nextDict.keysArray[0] = value
        #     elif numberOfAncestors == 5:
        #         i18nextDict.keysArray[0] = value
        #     elif numberOfAncestors == 6:
        #         i18nextDict.keysArray[0] = value
        #     elif numberOfAncestors == 7:
        #         i18nextDict.keysArray[0] = value
        #     elif numberOfAncestors == 8:
        #         i18nextDict.keysArray[0] = value

        #     return None


        try:
            lang = self.kwargs.get("lang")
            project = self.kwargs.get("project")
            translations_raw = Translation.objects.all().filter(language__code=lang, key__project__name=project)

            translation_list = list(translations_raw)

            translations_sortet_by_depth = sorted(translation_list, key=lambda d: d.key.get_depth())

            i18nextDict = dict()

            for translation in translations_sortet_by_depth:
                if translation.key.project.name == project and translation.language.code == lang:
                    keys = get_keys(translation)

                    # numberOfAncestors = len(keys)

                    i18nextDict = set_value_in_dict_recursive(i18nextDict, keys, translation.value)
                    print(i18nextDict)

            return Response(i18nextDict)
        except:
            print("ERROR")
            return Response({"error": "No translations found"})
