from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf.global_settings import LANGUAGES

class Language(models.Model):
    languages = models.CharField(max_length=7, blank=True)

    class Meta:
        ordering = ['languages']

    def __str__(self):
        return self.languages


class Project(models.Model):

    name = models.CharField(unique=True, db_index=True, max_length=255)
    languagees = models.ManyToManyField(Language, related_name='project')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name