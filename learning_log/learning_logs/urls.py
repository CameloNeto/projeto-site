"""Define os padrões de url para learning logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #pagina inicial
    path('',views.index,name='index'),
    #Pagina que mostra todos os tópicos
    path('topics/',views.topics,name='topics'),
    #Pagina de detalhes para um único tópico
    path('topics/<int:topic_id>/',views.topic,name='topic')
]