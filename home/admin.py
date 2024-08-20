
from django.contrib import admin
from django.utils.html import format_html
from .models import BannerImage, ReviewImage, SpecialOffer,CompanyInfo,CompanyVideo


@admin.register(BannerImage)
class BannerImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)

@admin.register(ReviewImage)
class ReviewImageAdmin(admin.ModelAdmin):
    list_display = ('alt_text',)

@admin.register(SpecialOffer)
class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('description',)

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = (('title', 'description') )

@admin.register(CompanyVideo)
class CompanyVideoAdmin(admin.ModelAdmin):
    list_display = ('company_info', 'description', 'video_link')

    def video_link(self, obj):
        if obj.video:
            return format_html('<a href="{0}" target="_blank">View Video</a>', obj.video.url)
        return 'No Video'
    video_link.short_description = 'Video'