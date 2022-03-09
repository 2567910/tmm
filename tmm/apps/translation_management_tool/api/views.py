from rest_framework.views import APIView
import json
from django.http import Http404
from tmm.apps.translation_management_tool.models import Translation, Project
from tmm.apps.translation_management_tool.api.serializer import TranslationsSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError, ParseError
from django.shortcuts import get_object_or_404

import logging

LOGGER = logging.getLogger(__name__)



def set_bulk_in_dict_recursive(i18nextDict, bulk, root_translation_list):

    for object in bulk:
        key = object["data"]["key"]
        root_translation = {}

        for root_translation in root_translation_list:
            if(root_translation.key.key == key):
                root_translation = root_translation
                break

        try:
            i18nextDict[key] = dict()
            set_bulk_in_dict_recursive(i18nextDict[key], object["children"], root_translation_list)

        except:
            i18nextDict[key] = root_translation.value

        root_translation_list.remove(root_translation)


    return i18nextDict


def translations_view(request, *args, **kwargs):

    lang = kwargs.get("lang")
    project_name = kwargs.get("project")

    #projectId = Project.objects.raw("SELECT id FROM translation_management_tool_project WHERE name = %s", [project_name])[0].id

    #translations_raw_sql_raw = Translation.objects.raw('SELECT * FROM translation_management_tool_translation WHERE key_id IN (SELECT id FROM translation_management_tool_translationkey WHERE project_id = %s) AND lang = %s', [projectId, lang])
    #translations_raw_sql_raw2 = Translation.objects.raw('SELECT * FROM translation_management_tool_translation WHERE (translation_management_tool_project.name =  %s AND translation_management_tool_language.code =  %s)', [projectId, lang])
    # .project = %s AND lang = %s', [projectId, lang])
    #('translation_management_tool_translationkey'.'depth' = 1 AND 'translation_management_tool_project'.'name' = 'test' AND 'translation_management_tool_language'.'code' = 'de')
    # LOGGER.info(translations_raw_sql_raw2)

    #LOG: statement: SELECT 'translation_management_tool_translation"."id", "translation_management_tool_translation"."key_id", "translation_management_tool_translation"."value", "translation_management_tool_translation"."language_id" FROM "translation_management_tool_translation" INNER JOIN "translation_management_tool_translationkey" ON ("translation_management_tool_translation"."key_id" = "translation_management_tool_translationkey"."id") INNER JOIN "translation_management_tool_project" ON ("translation_management_tool_translationkey"."project_id" = "translation_management_tool_project"."id") INNER JOIN "translation_management_tool_language" ON ("translation_management_tool_translation"."language_id" = "translation_management_tool_language"."id") WHERE ("translation_management_tool_translationkey"."depth" = 1 AND "translation_management_tool_project"."name" = 'test' AND "translation_management_tool_language"."code" = 'de')

    translations_raw = Translation.objects.filter(
        language__code=lang, key__project__name=project_name)
    translation_list = list(translations_raw)

    i18nextDict = dict()

    for translation in translation_list:
        LOGGER.info(translation.key.key)
        bulk = translation.key.dump_bulk(parent=translation.key, keep_ids=False)
        set_bulk_in_dict_recursive(i18nextDict, bulk, translation_list)


    if(len(i18nextDict) == 0): # if no translations found
        raise Http404("No translations found")

    response = JsonResponse(i18nextDict)
    return response
