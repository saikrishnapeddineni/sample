from django.contrib import admin

from fee.models import student


class b(admin.ModelAdmin):
    list_display=['name','fathername','contactnum','classname']
admin.site.register(student,b)
