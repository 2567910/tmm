from re import L
import json
from django.http import Http404
from tmm.apps.translation_management_tool.models import Translation, Project
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

import logging

LOGGER = logging.getLogger(__name__)


def set_values_in_dict_recursive(i18nextDict, path, translation, has_children):
    json_key = path[0]
    if len(path) == 1:
        if has_children:
            i18nextDict[json_key] = {}
        else:
            i18nextDict[json_key] = translation
    else:
        element = i18nextDict.get(json_key)
        if (element is None):
            i18nextDict[json_key] = dict()

        set_values_in_dict_recursive(
            i18nextDict[json_key], path[1:], translation, has_children)

    return i18nextDict


def translations_view(request, *args, **kwargs):
    lang = kwargs.get("lang")
    project_name = kwargs.get("project")
    i18nextDict = dict()

    for item in Translation.objects.filter(language__code=lang, key__project__name=project_name).select_related('key').order_by('key__key'):
        path = item.key.key.split('.')

        # set_values_in_dict_recursive(
        #     i18nextDict, path, item.value, item.key.has_children)

        name = path[-1]
        LOGGER.debug('>>>>>>>>>>>>>< processing %s', item.key.key)
        parent_names = path[:-1]
        if parent_names:
                direct_parent = None
                for parent_name in parent_names:
                    if direct_parent is None:
                        LOGGER.info("is has no direct_parent (is root node)")
                        parent = i18nextDict.setdefault(parent_name, {})
                        # parent= dict()
                    else:
                        LOGGER.info("This already has a direct parent: %s", direct_parent)
                        # parent = direct_parent[parent_name] = dict()
                        parent = direct_parent.setdefault(parent_name, {})
                    LOGGER.info('>>>>>>>>> loop parent %s (direct_parent %s): parent %s %s', parent_name, direct_parent, parent, type(parent))
                    direct_parent = parent
                LOGGER.info('>>>>>>>>>>>>>>> direct parent %s %s %s', direct_parent, type(direct_parent), type(name))
                direct_parent[name] = item.value
        else:
            LOGGER.info(item.value)
            i18nextDict[name] = item.value

    if(len(i18nextDict) == 0):  # if no translations found
        raise Http404("No translations found")

    response = JsonResponse(i18nextDict)
    return response


        # tree = {}
        # for item in Translation.objects.all():
        #     path = item.key.split('.')
        #     name = '_'.join(path[-1:], item.context)
        #     parent_names = path[:-1]
        #     if parent_names:
        #         direct_parent = None
        #         for parent_name in parent_names:
        #             if not direct_parent:
        #                 parent = tree.setdefault(parent_name, {})
        #             else:
        #                 parent = direct_parent.setdefault(parent_name, {})
        #             direct_parent = parent
        #         direct_parent[name] = value
        #     else:
        #         tree[name] = value
