from django.urls import path  
from .views import WELCOME
from .views import HOMEPAGE
from .views import LISTA
from .views import CHI_SIAMO
app_name = "prima app"
urlpatterns = [
    path('', HOMEPAGE, name = 'HOMEPAGE')
]

urlpatterns = [
    path('', WELCOME, name = 'WELCOME')
]

urlpatterns = [
    path('', LISTA, name = 'LISTA')
]
urlpatterns = [
    path('', CHI_SIAMO, name = 'CHI_SIAMO')
]