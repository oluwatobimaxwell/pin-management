from django.contrib import admin
from .models import Pin, Caller, Doctor


class CallerAdmin(admin.ModelAdmin):
    model = Caller
    list_display = ['name','gender', 'dob', 'address','occupation', 'education', 'symptoms', 'management']
    search_fields = ['name' ,'address','occupation', 'education', 'symptoms', 'management']
    list_per_page = 20
    list_filter = ('gender','dob', 'address','occupation', 'education', 'symptoms', 'management')






class PinAdmin(admin.ModelAdmin):
    model = Pin
    list_display = ['pin', 'value', 'location', 'batch', 'status', 'caller', 'phone', 'created_at', 'updated_at']
    search_fields = ['pin',]
    list_max_show_all = 100000
    list_per_page = 20
    list_filter = ('status','batch')
    # changelist_actions = ('Generate Pins', )
    # Change template data for the changelist view
    change_list_template = "admin/pin/Pin/change_list.html"

    def caller(self, pin):
        return pin.caller.name if (pin.caller != None) else "-"
      

    def phone(self, pin):
        return pin.caller.phone if (pin.caller != None) else "-"

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        pinIds = []
        pins = self.model.objects.all()
        for pin in pins:
            pinIds.append(str(pin.id))
        extra_context['pinIds'] = ','.join(pinIds)
        return super().changelist_view(request, extra_context=extra_context)

# Register your models here.
admin.site.register(Pin, PinAdmin)
admin.site.register(Caller, CallerAdmin)
admin.site.register(Doctor)


