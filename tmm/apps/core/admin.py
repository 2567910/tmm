from django.contrib import admin

from tmm.apps.core.models import Translations

from parler.admin import TranslatableAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from parler.admin import SortedRelatedFieldListFilter

# class ProjectAdmin(TranslatableAdmin):
#     list_display = (['key', 'value'])
#     fieldsets = (
#         (None, {
#             'fields': (['value']),
#         }),
#     )

# admin.site.register(Translations, ProjectAdmin)

class TranslationsResource(resources.ModelResource):

    class Meta:
        model = Translations
        # fields = ('key', 'value')

class TranslationsAdmin(TranslatableAdmin, ImportExportModelAdmin, ExportActionMixin):
    resources_class = TranslationsResource

    list_display = ('key', 'value')
    fieldsets = (
        (None, {
            'fields': ('key', 'translations__value'),
        }),
    )

    search_fields = ('translations__value', 'key')


admin.site.register(Translations, TranslationsAdmin)
