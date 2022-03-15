import unittest
from django.test import TestCase
import logging
from django.core import management

from tmm.apps.translation_management_tool.models import Language, Project, Translation, TranslationKey

LOGGER = logging.getLogger(__name__)

@unittest.skip
class ImportTest(TestCase):

    fixtures = ['project.json']

    def test_import(self):

        management.call_command('load_translations', './import_de.json', 'import', 'de')
        self.assertEqual(Translation.objects.count(), 38)

        nested_key = TranslationKey.objects.filter(depth=3).first()
        self.assertIsNotNone(nested_key)
        LOGGER.info('nested Key %s', nested_key)
        self.assertEqual(nested_key.key, "inner")

        value_of_key = nested_key.translation_set.filter(language__code = "de").first()
        # Translation.objects.filter(key=nested_key, language="en").first()
        # nested_key.translation_set.filter(language__code = "en").first()
        self.assertIsNotNone(value_of_key)
        LOGGER.info('Value of translation %s', value_of_key)
        self.assertEqual(value_of_key.value, "value")

        # management.call_command('load_translations', './import_de_1.json')
        # self.assertEqual(Translation.objects.count(), 38)

        # nested_key = TranslationKey.objects.filter(depth=3).first()
        # self.assertIsNotNone(nested_key)
        # LOGGER.info('nested Key %s', nested_key)
        # self.assertEqual(nested_key.key, "inner")