from django.conf.urls import url
from adm.views import ListaPublicadoresView

urlpatterns = [
    url(r'^publicadores/$',ListaPublicadoresView.as_view(template_name="adm/publicadores.html"), name="publicadores"),
]
