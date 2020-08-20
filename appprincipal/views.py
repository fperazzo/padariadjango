from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin #para Classes Based Views
from django.contrib.auth.decorators import login_required #para Functions Based Views


import json
import datetime

from projpad.models import TipoProduto, TipoCargo, Produto, Funcionario, Venda
#from appprincipal.forms import Orc_pt1_Form


# Create your views here.
class IndexTemplateView(TemplateView):
    template_name = "appprincipal/index.html"