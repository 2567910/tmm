from rest_framework.views import APIView
from tmm.apps.translation_management_tool.models import Translation, Project
from tmm.apps.translation_management_tool.api.serializer import TranslationsSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, ParseError

import logging

LOGGER = logging.getLogger(__name__)



def get_keys_from_ancestors(obj):
    ancestors = obj.key.get_ancestors()
    if ancestors:
        arr = [an.key for an in ancestors]
        arr.append(obj.key.key)
        return arr

    return [obj.key.key]


def set_value_in_dict_recursive(i18nextDict, keysArray, value):
    if (len(keysArray) == 1):
        i18nextDict[keysArray[0]] = value
    else:
        if (type(i18nextDict[keysArray[0]]) is not dict):
            i18nextDict[keysArray[0]] = dict()
        set_value_in_dict_recursive(
            i18nextDict[keysArray[0]], keysArray[1:], value)
    return i18nextDict


# class TranslationsView(APIView):
#     # GET /translations/project/lang
#     serializer_class = TranslationsSerializer

#     def get_queryset(self):
#         translations = Translation.objects.all()
#         return translations

def translations_view(request, *args, **kwargs):

    try:
        lang = kwargs.get("lang")
        project_name = kwargs.get("project")

        project = Project.objects.get_or_404(name=project_name)

        translations_raw = Translation.objects.filter(
            language__code=lang, key__project_id=project.id)
        translation_list = list(translations_raw)

        translations_sortet_by_depth = sorted(
            translation_list, key=lambda d: d.key.get_depth())

        i18nextDict = dict()

        # TEST Start --------------------------------------------------

        # for translation in translation_list:
        #     path = translation.key.path
        #     LOGGER.info('path %s', path)


        # only_root_translations = list(filter(lambda translation: translation.key.depth == 1, translation_list))

        # for translation in only_root_translations:
        #     LOGGER.info(translation.key.key)
        #     # keys = get_keys_from_ancestors(translation)
        #     test = translation.key.dump_bulk(parent=translation.key, keep_ids=True)
        #     LOGGER.info(test)
        #     keys = get_keys_from_ancestors(tanslation)
        #     set_value_in_dict_recursive(
        #         i18nextDict, keys, tanslation.value)


        # TEST END --------------------------------------------------

        for translation in translations_sortet_by_depth:
            keys = get_keys_from_ancestors(translation)

            i18nextDict = set_value_in_dict_recursive(
                i18nextDict, keys, translation.value)
            print(i18nextDict)

        if(len(i18nextDict) == 0): # if no translations found
            raise ValidationError

        return Response(i18nextDict)

    except:
        raise ValidationError