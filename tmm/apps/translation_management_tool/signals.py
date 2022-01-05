from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver

from tmm.apps.translation_management_tool.models import Translation, TranslationKey, Project, Language


@receiver(post_save, sender=TranslationKey)
def create_translations_for_langs (sender, instance, created, **kwargs):
    if created:
        for language in instance.project.languages.all():
            Translation.objects.create(language=language, key=instance)


@receiver(post_delete, sender=TranslationKey)
def create_translations_for_langs (sender, instance, **kwargs):
    for language in instance.project.languages.all():
        data_to_be_deleted = Translation.objects.filter(key = instance, language=language)
        data_to_be_deleted.delete()


        # https://docs.djangoproject.com/en/3.2/ref/signals/#:~:text=alias%20being%20used.-,m2m_changed,-%C2%B6
# If a new language is added to a project it sould
@receiver(m2m_changed, sender=Project.languages.through)
def create_translations_for_new_lang (sender, instance, pk_set, action, **kwargs):

    for changed_id in pk_set:
        all_keys_in_project = TranslationKey.objects.filter(project = instance)
        changed_lang = Language.objects.get(id = changed_id)

        for key in all_keys_in_project:
                if action == "pre_remove":
                    tranlsation_to_be_removed = Translation.objects.get(key = key, language = changed_lang)
                    tranlsation_to_be_removed.delete()

                if action == "pre_add":
                    Translation.objects.create(language= changed_lang, key = key)