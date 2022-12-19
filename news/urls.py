from django. urls import path
from .views import home, ArticoloDetailViewCB, ArticoloListViewCB, GiornalistaDetailViewCB, GiornalistaListViewCB #articoloDetailView 

app_name = 'news'

urlpatterns = [
    path("", home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail.html"),
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail.html"),
    path("lista_articoli/", ArticoloListViewCB.as_view(), name="lista_articoli"),
    path("giornalisti/<int:pk>/", GiornalistaDetailViewCB.as_view(), name="giornalista.detail"),
    path("lista_giornalisti/", GiornalistaListViewCB.as_view(), name="lista_giornalisti"),
]
