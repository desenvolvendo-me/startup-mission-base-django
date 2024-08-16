from django.contrib import admin
from .models import Meta, Task

class ListingMeta(admin.ModelAdmin):
    list_display= ("id", "nome")
    list_display_links= ("id", "nome")
admin.site.register(Meta, ListingMeta)




class ListingTask(admin.ModelAdmin):
    list_display= ("id", "name", "description", "meta", "user")
    list_display_links= ("id", "name")
admin.site.register(Task, ListingTask)


