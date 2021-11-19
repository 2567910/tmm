from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe

from django.conf.global_settings import LANGUAGES
from treebeard.mp_tree import MP_Node
from simple_history.models import HistoricalRecords
from simple_history import register



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


class TranslationKey(MP_Node): #
    key = models.CharField(max_length=255, help_text=mark_safe(
        "<b>Do not use the following endings in key: </b><br> $t(KEY_NAME) replace KEY_NAME with a  different translation key to use it in this translation</p>"
        + "<p><b>Interpolate: </b><br> {{VALUE}} replace VALUE with a variable that is defined for this translation.</p> "
        + "<p>For more information about the i18next value standart <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>"))
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    # node_order_by = ['key']
    class Meta:
        verbose_name = "Translationkey"
        verbose_name_plural = "Translationkeys"
        unique_together = ['project', 'key']

    # Translation.objects.create({})

    def __str__(self):
        return f"{self.key}"


class Translation(models.Model):

    key = models.ForeignKey(TranslationKey, on_delete=models.CASCADE)
    value = models.TextField(max_length=255,blank=True, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    history = HistoricalRecords()

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
