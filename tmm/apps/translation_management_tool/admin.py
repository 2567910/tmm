from django.contrib import admin


from tmm.apps.translation_management_tool.models import Project, Language, Translation, TranslationKey, JSONImport

from import_export.admin import ImportExportModelAdmin

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
    list_display = ('key', 'language', 'value')
    list_filter = (['language', 'key__project__name'])
    search_fields = (['value', 'key__key', 'key__project__name', 'language__code'])


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs:
            for tanslation in qs:
                if ((request.user == tanslation.key.project.translator.all()[0])):
                    return qs

                return qs.none()
        return qs.none()



    # @admin.display(description='Projekt', ordering='key__project')
    # def get_project_name(self, obj):
    #     return obj.key.project

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