from django.contrib import admin

from tmm.apps.core.models import Translations

from parler.admin import TranslatableAdmin
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field

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

    full_title = Field()

    t = Translations.objects.language("en").all()
    class Meta:
        model = Translations

    def dehydrate_full_title(self, translation):
        return '%s' % (translation.translations)

class TranslationsAdmin(TranslatableAdmin, ImportExportModelAdmin, ExportActionMixin):
    resources_class = TranslationsResource

    t = Translations.objects.language("en").all()
    # print (translations__value)

    list_display = ('key', 'value')
    fieldsets = (
        (None, {
            'fields': ('key', 'value'),
        }),
    )

    search_fields = ('translations__value', 'key')




admin.site.register(Translations, TranslationsAdmin)
