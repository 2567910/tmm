from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.conf.global_settings import LANGUAGES

class Language(models.Model):
    code = models.CharField(max_length=7, choices=LANGUAGES, blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Project(models.Model):

    name = models.CharField(unique=True, db_index=True, max_length=255)
    languages = models.ManyToManyField(Language)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class TranslationKey(models.Model):
    key = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Translationkey"
        verbose_name_plural = "Translationkeys"
        unique_together = ['project', 'key']

    def __str__(self):
        return f"{self.key} ({self.project})"


class Translation(models.Model):

    key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    # languagesForThisProject = ["1", "2", ""]
    # # Project.objects.get(name=project)


    # for label in languagesForThisProject: # AttributeError: 'ForeignKey' object has no attribute 'languages'
    #      locals()[label] = models.CharField(max_length=255, null=True, blank=True)

    #      del locals()['label']

    # print(projectLanguages)

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"
        unique_together = ['language', 'key']

    def __str__(self):
        return f"{self.key} {self.language}"