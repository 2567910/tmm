from django.contrib import admin
from django.db import transaction
from django.db import models
from django.contrib.admin import AdminSite
from django import forms
from django.core import management

from tmm.apps.translation_management_tool.models import Project, Language, Translation, TranslationKey, JSONImport

from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
# from tmm.apps.translation_management_tool.views import my_view
from import_export import resources
from import_export.fields import Field

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from simple_history.admin import SimpleHistoryAdmin

CONTENT_HELP_TEXT = ' '.join([
        "<p>For more information about the i18next value standart <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>"])

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_languages')
    search_fields = (['name'])

    @admin.display(description='Languages')
    def get_languages(self, obj):
        return ", ".join([lang.code for lang in obj.languages.all()])

class JSONImportAdmin(admin.ModelAdmin):
    readonly_fields = (['created_at'])
    list_display = ('created_at', 'project', 'language')
    search_fields = (['created_at', 'project', 'language'])

class TranslationsAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    readonly_fields = (['key', 'language'])
    list_display = ('key', 'get_project_name', 'language', 'value')
    list_filter = ('language', 'key__project')
    search_fields = (['key','get_project_name', 'language', 'value'])

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # qs.exclude(value=isinstance(value, dict))

        for tanslation in qs:
            if ((request.user == tanslation.key.project.translator.all()[0])):
                if (tanslation.key.has_children):
                    qs = qs.exclude(key__pk=tanslation.key.pk)
            else:
                return qs.none()
        return qs

    @admin.display(description='Projekt', ordering='key__project')
    def get_project_name(self, obj):
        return obj.key.project

    def has_add_permission(self, request, obj=None):
        return False

    # @admin.display(description='Key')
    # def get_full_key(self, obj):
    #     if (obj.key.get_ancestors()):
    #         return ".".join([lang.key for lang in obj.key.get_ancestors()]) + "." + obj.key.key
    #     else:
    #         return obj.key.key

    fieldsets = [
        ('Meta', {
            'fields':('key', 'language'),
        }),
        ('Value', {
            # 'orginal_text': '<div class="help">%s</div>' % CONTENT_HELP_TEXT,
            'fields':(['value']),
            'description': '<div class="help">%s</div>' % CONTENT_HELP_TEXT,
        }),
    ]
class TranslationKeyAdmin(admin.ModelAdmin):
    # readonly_fields = (['is_dict'])
    list_display = ('key', 'project')
    list_filter = (['project'])
    search_fields = (['key','project'])

admin.site.register(Translation, TranslationsAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(JSONImport, JSONImportAdmin)

admin.site.register(Language)

admin.site.register(TranslationKey, TranslationKeyAdmin)