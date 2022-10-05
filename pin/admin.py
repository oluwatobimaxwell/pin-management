from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from .models import Pin, Caller, Doctor
from pin.forms import CustomForm



class PinAdmin(admin.ModelAdmin):
    # list_display = ('pin',)
    search_fields = ['',]
    # form = CustomForm


# @staff_member_required
# def export(self, request):
#     return HttpResponseRedirect(request.META["HTTP_REFERER"])



# class MyAdmin(admin.ModelAdmin):
#      def has_add_permission(self, request, obj=None):
#         return False

# Register your models here.
admin.site.register(Pin, PinAdmin)
admin.site.register(Caller)
admin.site.register(Doctor)




# @admin.register(Pin)
# class FooAdmin(admin.ModelAdmin):
    