
from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "power_app"
urlpatterns = [
    # API rest
    path('', TemplateView.as_view(template_name='index.html')),
    path('usuario/<int:dni>', views.usuario, name="usuario"),
]