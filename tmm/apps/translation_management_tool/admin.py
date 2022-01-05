from django.contrib import admin
from django.db import transaction

from tmm.apps.translation_management_tool.models import Project, Language, Translation, TranslationKey


from import_export.admin import ImportExportModelAdmin
from import_export.admin import ExportActionMixin
from import_export import resources
from import_export.fields import Field

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from simple_history.admin import SimpleHistoryAdmin

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

    @admin.display(description='Languages')
    def get_languages(self, obj):
        return ", ".join([lang.code for lang in obj.languages.all()])




# class TranslationKeysAdmin(ImportExportModelAdmin, ExportActionMixin):

#     list_display = ('key', 'project', 'languages')
#     list_filter = ('language', 'key__project')
#     search_fields = (['key','get_project_name', 'language', 'value'])

#     @admin.display(description='Projekt', ordering='key__project')
#     def get_project_name(self, obj):
#         return obj.key.project

class TranslationsAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    # resources_class = TranslationsResource

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        final_qs = []
        # if request.user.is_superuser:
        #     return qs
        # else:

        #check if the key in queryset has a child element
        for tanslation in qs:
            print(TranslationKey.objects.get(pk=tanslation.key.pk).get_children())
            if TranslationKey.objects.get(pk=tanslation.key.pk).get_children():
                #This means the Trnaslation has no child elements
                qs = qs.exclude(key__pk=tanslation.key.pk)
                # qs.pop(tanslation)

        return qs


        # return qs.filter(key=1)

    # print (translations__value)

    list_display = ('get_full_key', 'get_project_name', 'language', 'value')

    list_filter = ('language', 'key__project')

    search_fields = (['key','get_project_name', 'language', 'value'])

    @admin.display(description='Projekt', ordering='key__project')
    def get_project_name(self, obj):
        return obj.key.project

    def has_add_permission(self, request, obj=None):
        return False

    @admin.display(description='Key')
    def get_full_key(self, obj):
        if (obj.key.get_ancestors()):
            return ".".join([lang.key for lang in obj.key.get_ancestors()]) + "." + obj.key.key
        else:
            return obj.key.key



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