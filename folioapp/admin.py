from django.contrib import admin
from .models import contact

# Register your models here.
class adminmodals(admin.ModelAdmin):
    list_display=['name','email','subject','message']


admin.site.register(contact,adminmodals)