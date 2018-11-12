from django.conf.urls import url
from bogotrash_app import views

urlpatterns = [
    url(r'^quejas/$', views.QuejaList.as_view()),
    url(r'^quejas/(?P<pk>[0-9]+)/$', views.QuejaDetail.as_view()),
    
    url(r'^catalogos/$', views.CatalogoList.as_view()),
    url(r'^catalogos/(?P<pk>[0-9]+)/$', views.CatalogoDetail.as_view()),
    
    url(r'^centros/$', views.CentroList.as_view()),
    url(r'^centros/(?P<pk>[0-9]+)/$', views.CentroDetail.as_view()),

    url(r'^desechos/$', views.DesechoList.as_view()),
    url(r'^desechos/(?P<pk>[0-9]+)/$', views.DesechoDetail.as_view()),
    
    url(r'^tipodesechos/$', views.TipoDesechoList.as_view()),
    url(r'^tipodesechos/(?P<pk>[0-9]+)/$', views.TipoDesechoDetail.as_view()),

    url(r'^usuarios/$', views.UsuarioList.as_view()),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
]
