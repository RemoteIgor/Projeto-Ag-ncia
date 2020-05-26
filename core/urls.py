from django.urls import path

#importa IndexView que esta em views
from .views import IndexView

#Cria rota
urlpatterns = [
    #Para rota principal executa IndexView como uma função e o nome dela é index
    path('', IndexView.as_view(), name='index'),
]