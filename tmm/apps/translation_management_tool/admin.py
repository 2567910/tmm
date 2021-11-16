from django.contrib import admin

from tmm.apps.translation_management_tool.models import Project, Language, Translation, TranslationKey


from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


CONTENT_HELP_TEXT = ' '.join(["<h4 style='padding-left: 0px; font-size: 15px'>Available options:</h4> <p>"
        + "<b>Nesting: </b><br> $t(KEY_NAME) replace KEY_NAME with a  different translation key to use it in this translation</p>"
        + "<p><b>Interpolate: </b><br> {{VALUE}} replace VALUE with a variable that is defined for this translation.</p> "
        + "<p>For more information about the i18next value standart <a href='https://www.i18next.com/misc/json-format' target='_blank'>click here</a>.</p>"])
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

class ProjectAdmin(admin.ModelAdmin):
    # resources_class = TranslationsResource


    # print (translations__value)

    list_display = ('name', 'get_languages')
    search_fields = (['name'])

    def get_languages(self, obj):
        return ", ".join([lang.code for lang in obj.languages.all()])




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

    def has_add_permission(self, request, obj=None):
        return False

    """
    Add your other customizations
    like actions, list_display, list filter, etc
    """
    fieldsets = [
        ('Meta', {
            'fields':('key', 'language'),
        }),
        ('Value', {
            'fields':(['value']),
            'description': '<div class="help">%s</div>' % CONTENT_HELP_TEXT,
        }),
    ]
    # def has_delete_permission(self, request, obj=None):
    #     return False

class TranslationKeyAdmin(TreeAdmin):
    # resources_class = TranslationsResource


    # print (translations__value)
    form = movenodeform_factory(TranslationKey)

    list_display = ('key', 'project')

    list_filter = (['project'])

    search_fields = (['key','project'])

admin.site.register(Translation, TranslationsAdmin)

admin.site.register(Project, ProjectAdmin)

admin.site.register(Language)

admin.site.register(TranslationKey, TranslationKeyAdmin)