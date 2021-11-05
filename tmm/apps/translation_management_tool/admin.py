from django.contrib import admin

from tmm.apps.translation_management_tool.models import Project


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




admin.site.register(Project, ProjectAdmin)
