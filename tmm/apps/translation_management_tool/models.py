from importlib.metadata import requires
from django.db import models
from django.core import management
from django.utils.safestring import mark_safe
from django.conf.global_settings import LANGUAGES
from treebeard.mp_tree import MP_Node
from simple_history.models import HistoricalRecords
from django.utils import timezone
from django.contrib.auth.models import User


class Language(models.Model):
    code = models.CharField(max_length=7, choices=LANGUAGES, blank=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.code


class Project(models.Model):
    name = models.CharField(unique=True, db_index=True, max_length=255)
    languages = models.ManyToManyField(Language)
    fallback_language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='+', null=True, blank=True)
    translator = models.ManyToManyField(User)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class TranslationKey(models.Model):
    key = models.CharField(max_length=255, help_text=mark_safe(
        "<p>v1.0.0 - For more information about the i18next value options <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    has_children = models.BooleanField(blank=True, default=False)

    class Meta:
        verbose_name = "Translationkey"
        verbose_name_plural = "Translationkeys"

    def __str__(self):
        return f"{self.key}"

class Translation(models.Model):
    key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
    value = models.TextField(blank=True, null=False, default="")
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Translation"
        verbose_name_plural = "Translations"
        unique_together = ['language', 'key']

    def __str__(self):
        return f"{self.key} {self.language}"

class JSONImport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    file = models.FileField()
    created_at = models.DateTimeField(default=timezone.now)

    def save(self):
        print(self.file.path)
        super().save()
        management.call_command('load_translations', self.file.path, self.language.code,  self.project.name)

    class Meta:
        verbose_name = "JSON Import"
        verbose_name_plural = "JSON Imports"
        unique_together = ['language', 'project', 'created_at']

    def __str__(self):
        return f"{self.project} {self.language} {self.created_at}"