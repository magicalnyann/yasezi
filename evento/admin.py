from django.contrib import admin
from .models import Evento, UserEvent

class EventoAdmin(admin.ModelAdmin):
    list_display = ['date', 'main_event', 'nyan_ncat', 'pok_pal', 'popup_1', 'popup_2']
    search_fields = [ 'date']
    list_filter = ['date']


class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'evento', 'date', 'points_awarded')
    list_filter = ('user', 'evento', 'date', 'points_awarded')
    fields = ['user', 'evento', 'date', 'points_awarded']


admin.site.register(Evento, EventoAdmin)
admin.site.register(UserEvent, UserEventAdmin)

