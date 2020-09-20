from django.contrib import admin

# Register your models here.
from projpad.models import TipoProduto, TipoCargo, Produto, Funcionario, Venda, Venda_Produto

admin.site.register(TipoProduto)
admin.site.register(TipoCargo)
admin.site.register(Produto)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Venda_Produto)
