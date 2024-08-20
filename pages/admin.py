from django.contrib import admin
from .models import Lounge
from django.utils.html import mark_safe

class LoungeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'pub_date')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_tag.short_description = 'Image Preview'

admin.site.register(Lounge, LoungeAdmin)