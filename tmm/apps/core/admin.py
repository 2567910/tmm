from django.contrib import admin

from tmm.apps.core.models import Translations

from parler.admin import TranslatableAdmin

# class ProjectAdmin(TranslatableAdmin):
#     list_display = (['key', 'value'])
#     fieldsets = (
#         (None, {
#             'fields': (['value']),
#         }),
#     )

# admin.site.register(Translations, ProjectAdmin)

@admin.register(Translations)
class TranslationsAdmin(TranslatableAdmin):
    list_display = (['key'])
