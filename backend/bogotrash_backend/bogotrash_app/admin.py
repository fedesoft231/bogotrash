from django.contrib import admin
from .models import *
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class MapaAdmin(admin.ModelAdmin):
    formfield_overrides = {
    map_fields.AddressField: {'widget':
    map_widgets.GoogleMapsAddressWidget},
 }

admin.site.register(Queja, MapaAdmin)

admin.site.register(Usuario)
admin.site.register(Catalogo)
admin.site.register(Desecho)
admin.site.register(Centro)
admin.site.register(TipoDesecho)