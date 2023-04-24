from django.contrib import admin
from enroll.models import student

class studentadmin(admin.ModelAdmin):
    list_display = ('id','stuname','stulocation')
# Register your models here.
admin.site.register(student,studentadmin)