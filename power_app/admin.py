from django.contrib import admin
from .models import *
from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render
from django.urls import path
from django.core.cache import cache
from .views import *

# esta importación es necesaria para el bucle for
# from django.apps import apps


class PowerAdminArea(admin.AdminSite):
    site_header = "Power Gym Administración"

power_site = PowerAdminArea(name="powerAdmin")

#? hasta ahi lo que hiciste fue crear una administración personalizada


# ? aca lo que haces es customize el formulario de django
class UsuarioModelForm(forms.ModelForm):
    DNI = forms.IntegerField(widget=forms.TextInput(attrs={'size': 10}))
    celular = forms.IntegerField(widget=forms.TextInput(attrs={'size': 10}), required=False)
    # estableces lo que esta permitdo por medio de una regular expresion
    # charfieldValidator = RegexValidator(r'^[a-zA-Z]*$', 'No puede ingresar números aquí.')
    # nombre = forms.CharField(max_length=50, validators=[charfieldValidator])
    # apellido=forms.CharField(max_length=50, validators=[charfieldValidator])

    class Meta:
        model = Usuario
        fields = '__all__'



class UsuarioAdmin(admin.ModelAdmin):
    list_display= ("nombre", "apellido", "sexo", "DNI", "celular", "pago", "vencimiento", "activo")
    ordering = ("-nombre", )
    list_filter =("activo",)
    # te hace la paginación:
    list_per_page = 10
    search_fields = ("nombre", "apellido","DNI",)
    search_help_text = "Buscar por nombre, apelido o DNI"
    actions = ['mark_as_published', 'mark_as_unpublished']
    change_list_template = 'change_list_usuarios.html'

    # list_editable = ( "apellido", "sexo", "DNI", "celular", "pago", "vencimiento")

    form = UsuarioModelForm

    def update_activo(self, obj):
        if obj.vencimiento < timezone.now().date():
            obj.activo = False
        else:
            obj.activo = True
        obj.save()

    update_activo.short_description = "Update Activo"

    # the changelist_view method checks the last execution date stored in the cache (update_activo_last_execution_date). If it is different from the current date, the update_activo function is called for each object in the queryset, and the activo field is updated accordingly. After the execution, the current date is stored in the cache as the last execution date.
    def changelist_view(self, request, extra_context=None):
        last_execution_date = cache.get('update_activo_last_execution_date')
        current_date = timezone.now().date()

        if last_execution_date != current_date:
            queryset = self.get_queryset(request)
            for obj in queryset:
                self.update_activo(obj)

            cache.set('update_activo_last_execution_date', current_date)

        return super().changelist_view(request, extra_context=extra_context)


    def get_urls(self):
        urls = super().get_urls()
        # lo que haces aca es crear este path y que cuando se lo llame se ejecute la función upload
        new_urls = [path('upload-excel/', upload_excel), path('graphics/', graphics)]
        return new_urls + urls


class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("usuario","dia", "hora", "activo")
    list_filter =("dia","activo")
    search_fields = ("usuario",)
    search_help_text = "Buscar por nombre"
    list_per_page = 10
    ordering = ("-dia", )

    


power_site.register(Usuario, UsuarioAdmin)
power_site.register(Asistencia, AsistenciaAdmin)

# esto que haces es para no tener que registrar los modelos uno por uno
# models = apps.get_models()
# for model in models:
#     try:
#         power_site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass


