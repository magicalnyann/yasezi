from django.contrib import admin
from .models import Lounge, Comments, Reply
from django.utils.html import mark_safe


@admin.register(Lounge)
class LoungeAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'pub_date')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return '-'
    image_tag.short_description = 'Image Preview'

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_list', 'content', 'create_date', 'heart', 'parent', 'image_tag')
    search_fields = ('content',)
    list_filter = ('create_date', 'author', 'content_list')
    fields = ('author', 'content_list', 'content', 'create_date', 'heart', 'parent', 'image')
    readonly_fields = ('create_date', 'image_tag') 

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return '-'
    image_tag.short_description = 'Image Preview'

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_list', 'content', 'create_date', 'heart', 'parent_comment', 'image_tag')
    search_fields = ('content',)
    list_filter = ('create_date', 'author', 'content_list')
    fields = ('author', 'content_list', 'content', 'create_date', 'heart', 'parent_comment', 'image')
    readonly_fields = ('create_date', 'image_tag') 

    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        return '-'
    image_tag.short_description = 'Image Preview'