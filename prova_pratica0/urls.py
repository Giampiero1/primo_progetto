from django.urls import path
from .views import index0, maxmin,media

app_name="prova_pratica0"

urlpatterns=[
    path('index0/',index0,name="index0"),
    path('maxmin/',maxmin,name="maxmin"),
    path('media/',media,name="media"),
]