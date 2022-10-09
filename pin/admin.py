from django.contrib import admin
from .models import Pin, Caller, Doctor

class PinAdmin(admin.ModelAdmin):
    model = Pin
    list_display = ['pin', 'status', 'caller', 'phone', 'created_at', 'updated_at']
    search_fields = ['pin',]  
    list_per_page = 20
    list_filter = ('status',)
    changelist_actions = ('Generate Pins', )
    change_list_template = "admin/pin/Pin/change_list.html"

    def caller(self, pin):
        return pin.caller.name if (pin.caller != None) else "-"
      

    def phone(self, pin):
        return pin.caller.phone if (pin.caller != None) else "-"


# Register your models here.
admin.site.register(Pin, PinAdmin)
admin.site.register(Caller)
admin.site.register(Doctor)


