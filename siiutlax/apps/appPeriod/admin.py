from django.contrib import admin
from .models import Period,Semester

@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display=['year', 'period', 'cycle','is_active']
    list_editable=['is_active']
    
@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display=['semester_name']




