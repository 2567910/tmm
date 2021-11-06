from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf.global_settings import LANGUAGES

class Language(models.Model):
    languages = models.CharField(max_length=7, choices=LANGUAGES, blank=True)

    class Meta:
        ordering = ['languages']

    def __str__(self):
        return self.languages


class Project(models.Model):

    name = models.CharField(unique=True, db_index=True, max_length=255)
    languages = models.ManyToManyField(Language)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Translation(models.Model):

    key = models.CharField(unique=True, db_index=True, max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    for label in project.languages: # AttributeError: 'ForeignKey' object has no attribute 'languages'
         locals()[label] = models.CharField(max_length=255, null=True, blank=True)

         del locals()['label']

    # print(projectLanguages)

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"

    def __str__(self):
        return self.key
