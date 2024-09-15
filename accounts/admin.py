from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'phone_number', 'points']
    readonly_fields = ['points']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []  # 슈퍼유저는 모든 필드를 수정할 수 있도록
        return self.readonly_fields

admin.site.register(Profile, ProfileAdmin)