from django.contrib import admin

from tmm.apps.translation_management_tool.models import Project, Language, Translation, TranslationKey


from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field



# class ProjectAdmin(TranslatableAdmin):
#     list_display = (['key', 'value'])
#     fieldsets = (
#         (None, {
#             'fields': (['value']),
#         }),
#     )

# admin.site.register(Translations, ProjectAdmin)

# class TranslationsResource(resources.ModelResource):

#     full_title = Field()

#     t = Translations.objects.language("en").all()
#     class Meta:
#         model = Translations

#     def dehydrate_full_title(self, translation):
#         return '%s' % (translation.translations)

class ProjectAdmin(ImportExportModelAdmin, ExportActionMixin):
    # resources_class = TranslationsResource


    # print (translations__value)

    list_display = (['name'])

    search_fields = (['name'])

# class TranslationKeysAdmin(ImportExportModelAdmin, ExportActionMixin):

#     list_display = ('key', 'project', 'languages')
#     list_filter = ('language', 'key__project')
#     search_fields = (['key','get_project_name', 'language', 'value'])

#     @admin.display(description='Projekt', ordering='key__project')
#     def get_project_name(self, obj):
#         return obj.key.project

class TranslationsAdmin(ImportExportModelAdmin, ExportActionMixin):
    # resources_class = TranslationsResource


    # print (translations__value)

    list_display = ('key', 'get_project_name', 'language', 'value')

    list_filter = ('language', 'key__project')

    search_fields = (['key','get_project_name', 'language', 'value'])

    @admin.display(description='Projekt', ordering='key__project')
    def get_project_name(self, obj):
        return obj.key.project

admin.site.register(Translation, TranslationsAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Language)

admin.site.register(TranslationKey)