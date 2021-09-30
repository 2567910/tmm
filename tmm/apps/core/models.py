from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields



class Translations(TranslatableModel):

    key = models.CharField(_("Key"), unique=True, db_index=True, max_length=255)

    translations = TranslatedFields(
        value = models.TextField()
    )

    class Meta:
        verbose_name = _("Translation")
        verbose_name_plural = _("Translations")
    def __str__(self):
        return self.value