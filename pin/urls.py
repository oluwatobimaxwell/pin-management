from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('generate/', views.generate_pin_form, name='generate'),
    path('generate-create/', views.generate_pin, name='create-pins'),
    path('print-pins/', views.print_pins, name='print-pins'),
]

urlpatterns += staticfiles_urlpatterns()