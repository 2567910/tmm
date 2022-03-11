import json
import logging
import os

from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction
from tmm.apps.translation_management_tool.models import Project, TranslationKey, Translation, Language


LOGGER = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Load translations from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        parser.add_argument('lang', type=str)
        parser.add_argument('project', type=str)
        parser.add_argument('--clear', '-c', action='store_true',
                            help='Clear existing objects before loading')

    def handle(self, *args, **options):
        resultDict = {}
        filepath = options['file']
        LOGGER.info('Loading tags from %s ...', filepath)
        with transaction.atomic():
            with open(filepath, 'r') as json_in:
                rawDict = json.load(json_in)
                project_name = options['project']
                lang_str = options['lang']

                project = Project.objects.filter(name=project_name).first()
                if not project:
                    raise Exception('Project does not exist: ', project_name)

                lang = Language.objects.filter(code=lang_str).first()
                if not lang:
                    raise Exception('Language does not exist: ', lang_str)

                if options['clear']:
                    deleted = Translation.objects.filter(key__project=project, language=lang).delete()

                for raw_key, raw_value in rawDict.items():
                    print(raw_key, raw_value) # this is only th root Key
                    root_key = TranslationKey.objects.filter(key=raw_key, project=project).first()

                    if not root_key:
                        root_key = TranslationKey.objects.create(key=raw_key, project=project)

                    if isinstance(raw_value, str):
                        Translation.objects.filter(key=root_key, language=lang).update(value=raw_value)

                    elif isinstance(raw_value, dict):
                        # recurse into children
                        self.create_child(root_key, raw_value, lang)
                    else:
                        raise Exception('Expecting string or dictionary but got', raw_value)

                    if (type(rawDict[raw_key]) is not dict):
                        resultDict[raw_key] = {"value": rawDict, "parent": None}


    def create_child(self, parent_node: TranslationKey, raw_dict: dict, lang: Language):
        parent_node.has_children = True
        parent_node.save()

        for child_key, child_value in raw_dict.items():
            full_child_key = parent_node.key + '.' + child_key
            child_node = TranslationKey.objects.filter(key=full_child_key, project=parent_node.project).first()

            if not child_node:
                child_node = TranslationKey.objects.create(key=full_child_key, project=parent_node.project)

            if isinstance(child_value, str):
                Translation.objects.filter(key=child_node, language=lang).update(value=child_value)

            elif isinstance(child_value, dict):
                self.create_child(child_node, child_value, lang)
            else:
                raise Exception('Expecting string or dictionary but got %s for key %s', child_value, child_key)
