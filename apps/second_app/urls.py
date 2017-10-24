from django.conf.urls import url
from . import views    

urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^add_pet$', views.addPet),
    url(r'^created$', views.createPet),
    url(r'^delete/(?P<id>\d+)$', views.deletePet),
    url(r'^show/(?P<id>\d+)$', views.showUser),
    
]