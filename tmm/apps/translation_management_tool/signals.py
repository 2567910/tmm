from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver

from tmm.apps.translation_management_tool.models import Translation, TranslationKey, Project, Language
import logging

LOGGER = logging.getLogger(__name__)
# If a new translation key is added, create a new translation for each language
@receiver(post_save, sender=TranslationKey)
def create_translations_for_langs (sender, instance, created, **kwargs):
    LOGGER.info('In create_translations_for_langs signal')
    if created:
        for language in instance.project.languages.all():
            Translation.objects.create(language=language, key=instance)

# If a translation key is deleted, delete all translations for that key
@receiver(post_delete, sender=TranslationKey)
def delete_translations_for_langs (sender, instance, **kwargs):
    LOGGER.info('delete_translations_for_langs')
    for language in instance.project.languages.all():
        data_to_be_deleted = Translation.objects.filter(key = instance, language=language)
        data_to_be_deleted.delete()

# If a new language is added to a project then we need to create a translation for each translation key
@receiver(m2m_changed, sender=Project.languages.through)
def create_translations_for_new_lang (sender, instance, pk_set, action, **kwargs):
    LOGGER.info('create_translations_for_new_lang')
    for changed_id in pk_set:
        all_keys_in_project = TranslationKey.objects.filter(project = instance)
        changed_lang = Language.objects.get(id = changed_id)

        for key in all_keys_in_project:
                if action == "pre_remove":
                    tranlsation_to_be_removed = Translation.objects.get(key = key, language = changed_lang)
                    tranlsation_to_be_removed.delete()

                if action == "pre_add":
                    Translation.objects.create(language= changed_lang, key = key)