from re import L
import json
from django.http import Http404
from tmm.apps.translation_management_tool.models import Translation, Project
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

import logging

LOGGER = logging.getLogger(__name__)

def translations_view(request, *args, **kwargs):
    lang = kwargs.get("lang")
    project_name = kwargs.get("project")
    i18nextDict = dict()

    for item in Translation.objects.filter(language__code=lang, key__project__name=project_name).select_related('key'):
        path = item.key.key.split('.')

        name = path[-1]
        parent_names = path[:-1]
        if parent_names:
                direct_parent = None
                for parent_name in parent_names:
                    if direct_parent is None:
                        parent = i18nextDict.setdefault(parent_name, {})
                    else:
                        parent = direct_parent.setdefault(parent_name, {})
                    direct_parent = parent
                direct_parent[name] = item.value
        else:
            LOGGER.info(item.value)
            i18nextDict[name] = item.value

    if(len(i18nextDict) == 0):  # if no translations found
        raise Http404("No translations found")

    response = JsonResponse(i18nextDict)
    return response