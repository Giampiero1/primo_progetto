from django.urls import path
from .views import views_a, views_b

app_name="prova_pratica2"

urlpatterns=[
    path('views_a/',views_a,name="lista_targhe"),
    path('views_b/',views_b,name="lista_noleggi"),
]