#from core.views import LocaisList, IndexTemplateView, LocalDetailView, RegCreateView, Pt1CreateView
from . import views
from appprincipal.views import IndexTemplateView,  AboutView, TermoView, PolView, ContView,  NewVendaCreateView, ProdListView, RegistrarTipoProdutoForm, Cadast_TipoProdCreateView
from django.urls import path
from appprincipal.views import *

app_name = 'appprincipal'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name = 'index'),
    path('about/', AboutView.as_view(), name = "about"),
    path('minhasvendas/', ProdListView.as_view(), name="lista"),
    path('cargo/funcionario', FuncionarioCreateView.as_view(), name="func_cad"),
    path('cargo/', CargoCreateView.as_view(), name="cargo"),
    path('novavenda/', NewVendaCreateView.as_view(), name ="nova_venda"),
    path('termo_cond/', TermoView.as_view(), name="termo_cond"),
    path('pol/', PolView.as_view(), name="pol"),
    path('cont/', ContView.as_view(), name="cont"),
    path('minhasvendas/excluir/<pk>', VendaDeleteView.as_view(), name = 'deleta_venda'),
    path('tipoprod/', Cadast_TipoProdCreateView.as_view(), name="tipoprod"),
    path('tipoprod/produto/', Cadast_ProdCreateView.as_view(), name = 'produto'),
    path('listavenda/', VendProdListView.as_view(), name="lista_venda"),
]