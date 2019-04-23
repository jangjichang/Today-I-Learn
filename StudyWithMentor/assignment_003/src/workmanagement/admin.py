from django.contrib import admin
from .models import WorkList, Card, Activity


# Register your models here.

class WorkListAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'worklist']


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['description', 'owner']


admin.site.register(WorkList, WorkListAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Activity, ActivityAdmin)