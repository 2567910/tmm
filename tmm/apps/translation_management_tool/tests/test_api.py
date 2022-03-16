from django.test import TestCase
import logging
from django.urls import reverse

from tmm.apps.translation_management_tool.models import Language, Project, Translation, TranslationKey


LOGGER = logging.getLogger(__name__)

class ApiTest(TestCase):

    fixtures = ['project.json']

    TEST_I18N = {
        "title": "Test-Titel",
        "common": {
            "actions": {
                "save": "Speichern"
            },
            "ok": "OK"
        }
    }

    def test_json_output(self):
        project = Project.objects.first()
        self.assertIsNotNone(project)
        lang_de = Language.objects.get(code='de')

        key_title = TranslationKey.objects.create(key='title', project=project)
        self.assertEqual(Translation.objects.count(), 2, Translation.objects.values())
        Translation.objects.filter(key=key_title, language=lang_de).update(value='Test-Titel')

        key_save = TranslationKey.objects.create(key='common.actions.save', project=project)
        Translation.objects.filter(key=key_save, language=lang_de).update(value='Speichern')

        key_ok = TranslationKey.objects.create(key='common.ok', project=project)
        Translation.objects.filter(key=key_ok, language=lang_de).update(value='OK')

        response = self.client.get(reverse('i18next_json', kwargs={'project': project.name, 'lang': 'de'}))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        LOGGER.debug('>>>>>>>>>> expected %s', self.TEST_I18N)
        LOGGER.debug('>>>>>>>>>> actual   %s', data)
        self.assertDictEqual(data, self.TEST_I18N)
