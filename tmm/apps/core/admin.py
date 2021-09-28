from django.contrib import admin

from tmm.apps.core.models import Person, Course, Grade, Test

from parler.admin import TranslatableAdmin

class ProjectAdmin(TranslatableAdmin):
    list_display = ('name', 'year')
    fieldsets = (
        (None, {
            'fields': ('name', 'year'),
        }),
    )

admin.site.register(Test, ProjectAdmin)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

# @admin.register(Test)
# class TestAdmin(admin.ModelAdmin):
#     pass