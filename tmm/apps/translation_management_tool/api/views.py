from re import L
from rest_framework.views import APIView
import json
from django.http import Http404
from tmm.apps.translation_management_tool.models import Translation, Project
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError, ParseError
from django.shortcuts import get_object_or_404

import logging

LOGGER = logging.getLogger(__name__)

def set_values_in_dict_recursive(i18nextDict, keysArray, value, has_children):
    if (len(keysArray) == 1):
        if(has_children):
            i18nextDict[keysArray[0]] = {}
        else:
            i18nextDict[keysArray[0]] = value
    else:
        element = i18nextDict.get(keysArray[0])
        if (element is None):
            i18nextDict[keysArray[0]] = dict()

        set_values_in_dict_recursive(i18nextDict[keysArray[0]], keysArray[1:], value, has_children)

    return i18nextDict

def translations_view(request, *args, **kwargs):
    lang = kwargs.get("lang")
    project_name = kwargs.get("project")
    i18nextDict = dict()

    for item in Translation.objects.filter(language__code=lang, key__project__name=project_name):
        keys = item.key.key.split('.')

        set_values_in_dict_recursive(i18nextDict, keys, item.value, item.key.has_children)

    if(len(i18nextDict) == 0): # if no translations found
        raise Http404("No translations found")

    response = JsonResponse(i18nextDict)
    return response




# name = path[-1:]
        # parent_names = path[:-1]
        # if parent_names:
        #     direct_parent = None
        #     for parent_name in parent_names:
        #         LOGGER.info(parent_names)
        #         if not direct_parent:
        #             LOGGER.info("is has no direct_parent (is root node)")
        #             parent = i18nextDict[parent_name] = dict()
        #             # i18nextDict.setdefault(parent_name, dict())
        #             # parent = i18nextDict[parent_name]
        #         else:
        #             LOGGER.info("This already has a direct parent")
        #             # parent = direct_parent[parent_name] = dict()
        #             parent = direct_parent.setdefault(parent_name, {})
        #         direct_parent = parent
        #     LOGGER.info(direct_parent)
        #     direct_parent[name[0]] = item.value
        # else:
        #     LOGGER.info(item.value)
        #     i18nextDict[name[0]] = item.value