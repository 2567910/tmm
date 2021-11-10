from django.db.models.signals import post_save
from django.dispatch import receiver

from tmm.apps.translation_management_tool.models import Translation, TranslationKey, Project, Language


@receiver(post_save, sender=TranslationKey)
def create_translations_for_langs (sender, instance, created, **kwargs):
    if created:
        for language in instance.project.languages.all():
            Translation.objects.create(
                language= language,
                key = instance,
                )