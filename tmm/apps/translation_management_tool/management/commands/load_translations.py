import json
import logging

from django.apps import apps
from django.core.management import BaseCommand
from django.db import transaction


LOGGER = logging.getLogger(__name__)

# Write a custom command to load translations from a json file  into the database



class Command(BaseCommand):
    help = 'Load translations from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)
        parser.add_argument('--clear', '-c', action='store_true',
                            help='remove existing tags before import')

    def handle(self, *args, **options):
        filename = options['file']
        LOGGER.info('Loading tags from %s ...', filename)
        with transaction.atomic():
            # if options['clear']:
            # Clear objects in database
            count = 0
            rel_count = 0
            with open(filename, 'r') as json_in:
                data_list = json.load(json_in)
                LOGGER.info('Loaded %s translations', data_list)
                # for data in data_list:
                #     model = apps.get_model(data['model'])