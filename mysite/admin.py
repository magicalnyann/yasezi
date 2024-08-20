from django.contrib import admin
from .models import MainContent, Comment, RecommProduct
from django.utils.html import mark_safe
class MainContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image_tag', 'pub_date')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_tag.short_description = 'Image Preview'

class RecommProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'image_tag', 'pub_date')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_tag.short_description = 'Image Preview'

admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Comment)
admin.site.register(RecommProduct, RecommProductAdmin)
