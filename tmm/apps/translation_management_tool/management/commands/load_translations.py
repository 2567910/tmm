import json
import logging
import os

from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction
from tmm.apps.translation_management_tool.models import Project, TranslationKey, Translation, Language


LOGGER = logging.getLogger(__name__)


#./manage.py load_translations import_de.json



class LoadTranslationsCommand(BaseCommand):
    help = 'Load translations from JSON file'


    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        parser.add_argument('--clear', '-c', action='store_true',
                            help='Clear existing objects before loading')

    def handle(self, *args, **options):

        resultDict = {}

        # def get_formated_data_recursive(formatedDict, key, value):
        #     if (type(rawDict[key]) is not dict):
        #         formatedDict[keysArray[0]] = value
        #     else:
        #         if (type(formatedDict[keysArray[0]]) is not dict):
        #             formatedDict[keysArray[0]] = dict()
        #         get_formated_data_recursive(
        #             formatedDict[keysArray[0]], keysArray[1:], value)
        #     return formatedDict

        filepath = options['file']
        LOGGER.info('Loading tags from %s ...', filepath)
        with transaction.atomic():
            with open(filepath, 'r') as json_in:
                rawDict = json.load(json_in)

                filename = os.path.basename(filepath)
                project_lang = os.path.splitext(filename)[0]
                project_and_lang = project_lang.split('_')  # returns array
                project_name = project_and_lang[0]
                lang_str = project_and_lang[1]


                LOGGER.info('Loading translation for project %s and language %s...', project_name, lang_str)

                project = Project.objects.filter(name=project_name).first()
                if not project:
                    raise Exception('Project does not exist: ', project_name)

                lang = Language.objects.filter(code=lang_str).first()
                if not lang:
                    raise Exception('Language does not exist: ', lang_str)

                if options['clear']:
                    LOGGER.warning('DELETING translations for project %s and language %s', project, lang)
                    deleted = Translation.objects.filter(key__project=project, language=lang).delete()
                    LOGGER.warning('DELETED %d translations', deleted[0])


                for raw_key, raw_value in rawDict.items():  # root/namespace level, e.g. "general"
                    LOGGER.debug('>>> in loop --- %s : %s', raw_key, raw_value)

                    root_key = TranslationKey.objects.filter(key=raw_key, project=project, depth=1).first()
                    if not root_key:
                        root_key = TranslationKey.add_root(key=raw_key, project=project)
                    LOGGER.debug('>>> adding root %s', root_key)

                    if isinstance(raw_value, str):
                        # this is a translation
                        LOGGER.debug('>>> sinstance if str %s - %s: %s', lang, root_key, raw_value)
                        Translation.objects.filter(key=root_key, language=lang).update(value=raw_value)

                        LOGGER.debug('>>> adding translation %s - %s: %s', lang, root_key, raw_value)
                    elif isinstance(raw_value, dict):
                        LOGGER.debug('>>> is dict --- %s : %s', raw_value, raw_value)
                        # recurse into children
                        self.create_child(root_key, raw_value, lang)
                    else:
                        raise Exception('Expecting string or dictionary but got', raw_value)

                    # resultDict = get_formated_data_recursive(resultDict, key, rawDict[key])
                    if (type(rawDict[raw_key]) is not dict):
                        resultDict[raw_key] = {"value": rawDict, "parent": None}
                        print("key: ", raw_key, " value: ", rawDict[raw_key], " No parents")

                    # print(key, rawDict)
                    # get_formated_data_recursive()
                    # print(data.get('model'))
                    # load_data_recursive(data, None)
                    # Translation.objects.bulk_create(new_objects) # good performance for real production/large files

    def create_child(self, parent_node: TranslationKey, raw_dict: dict, lang: Language):
        for child_key, child_value in raw_dict.items():
            child_node = parent_node.get_children().filter(key=child_key, project=parent_node.project).first()
            if not child_node:
                child_node = parent_node.add_child(key=child_key, project=parent_node.project)
            LOGGER.debug('>>> adding child %s', child_node.key)
            if isinstance(child_value, str):
                # this is a translation
                LOGGER.debug('>>> adding child %s', child_node)
                # Translation.objects.create(key=child_node, value=child_value, language=lang)
                Translation.objects.filter(key=child_node, language=lang).update(value=child_value)
                LOGGER.debug('>>> adding translation %s - %s: %s', lang, child_node, child_value)
            elif isinstance(child_value, dict):
                self.create_child(child_node, child_value, lang)
            else:
                raise Exception('Expecting string or dictionary but got %s for key %s', child_value, child_key)
