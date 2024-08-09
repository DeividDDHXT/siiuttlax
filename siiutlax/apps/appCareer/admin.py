from django.contrib import admin

from apps.appCareer.models import Career, Subject


# Register your models here.
@admin.register(Career)
class Career(admin.ModelAdmin):
    list_display = ['short_name', 'level', 'name']
    ordering = ['level', 'short_name']

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'career', 'semester','weekly_hours', 'total_hours']
    ordering = ['career', 'semester']