from django.contrib import admin

from .models.upload import Upload
@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'age', 'gender', 'brief_history',
                    'symptoms', 'clinical_diagnosis', 'file', 'creation_date']
    list_filter = ['creation_date']
