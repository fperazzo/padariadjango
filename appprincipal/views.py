from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from projpad.models import *
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views
from appprincipal import views
from appprincipal.forms import *


import json
import datetime

from projpad.models import TipoProduto, TipoCargo, Produto, Funcionario, Venda


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "index.html"

class ProdListView(ListView):
    template_name = "vendas.html"
    model = Produto
    context_object_name = "produtos"
    

class AboutView(View):
    template = "about.html"
    def get (self, request):

        return render(request, self.template)

class Cadast_TipoProdCreateView(CreateView):
    template_name = "cadast_prod.html"
    model = TipoProduto
    form_class = RegistrarTipoProdutoForm
    success_url = reverse_lazy("appprincipal:produto")

class Cadast_ProdCreateView(CreateView):
    template_name = "prod_cad.html"
    model = Produto
    form_class = RegistrarProdutoForm
    success_url = reverse_lazy("appprincipal:index")

class ProdListView(ListView):
    template_name = "vendas.html"
    model = Produto
    context_object_name = "produtos"

class CargoCreateView(CreateView):
    template_name = "cadast_cargo.html"
    model = TipoCargo
    form_class = CargoForm
    success_url = reverse_lazy("appprincipal:index")

class FuncionarioCreateView(CreateView):
    template_name = "cadastrar_func.html"
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy("appprincipal:index")

class NewVendaCreateView(CreateView):
    template_name = "nova_venda.html"
    model = Venda
    form_class = RegistrarVendaForm
    success_url = reverse_lazy("appprincipal:index")

class TermoView(View):
    template = "termo.html"
    def get (self, request):

        return render(request, self.template)

class PolView(View):
    template = "pol.html"
    def get (self, request):

        return render(request, self.template)

class ContView(View):
    template = "cont.html"
    def get (self, request):

        return render(request, self.template)

class VendaDeleteView(DeleteView):
    template_name = "exclui_venda.html"
    model = Produto
    context_object_name =  'produto'
    success_url = reverse_lazy("appprincipal:index")

class VendaCreateView(CreateView):
    template_name = "venda.html"
    model = Venda_Produto
    context_object_name =  'venda_produtos'
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:index")

class VendProdListView(ListView):
    template_name = "venda_prod.html"
    model = Venda_Produto
    context_object_name = "lista_venda"

class FuncionarioUpdateView(UpdateView):
    template_name = "atualiza_func.html"
    model = Funcionario
    context_object_name = "funcionario"
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:lista_funcionarios")

class ListaFuncionariosListView(ListView):
    template_name = "funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"

class FuncionarioDeleteView(DeleteView):
    template_name = "exclui_func.html"
    model = Funcionario
    context_object_name =  'funcionario'
    success_url = reverse_lazy("appprincipal:lista_funcionarios")

class ListaProdutoListView(ListView):
    template_name = "produtos.html"
    model = Produto
    context_object_name = "produtos"

class ProdutoUpdateView(UpdateView):
    template_name = "atualiza_prod.html"
    model = Produto
    context_object_name = "produto"
    fields = '__all__'
    success_url = reverse_lazy("appprincipal:lista_produto")

class ProdutoDeleteView(DeleteView):
    template_name = "exclui_prod.html"
    model = Produto
    context_object_name =  'produto'
    success_url = reverse_lazy("appprincipal:lista_produto")
    