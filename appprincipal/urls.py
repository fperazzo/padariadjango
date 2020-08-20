#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from appprincipal.views import IndexTemplateView
from django.urls import path
from . import views

app_name = 'appprincipal'

urlpatterns = [


    path('', IndexTemplateView.as_view(), name="index"),
    # path('lorcchave/', views.lista_orc_chave, name="lista_orc_chave"),
    # path('pt1/', views.pt1_new, name='pt1'),


 ]