from django.urls import path  
from .views import welcome
from .views import homepage
from .views import lista
from .views import chi_siamo
from .views import variabili
from .views import index
app_name = "prima app"
urlpatterns = [
    path('', homepage, name = 'homepage'),
    path('', welcome, name = 'welcome'),
    path('', lista, name = 'lista'),
    path('', chi_siamo, name = 'chi_siamo'),
    path('', variabili, name = 'variabili'),
    path('', index, name = 'index'),
]

