from projpad.models import *
from django import forms

class CargoForm(forms.ModelForm):

    class Meta:
        model = TipoCargo

        fields = [
            'nmtipocargo',
        ]

class FuncionarioForm(forms.ModelForm):

    class Meta:
        model = Funcionario

        fields = [
            'fkcargo',
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao',
        ]


class RegistrarTipoProdutoForm(forms.ModelForm):
    
    class Meta:
        model = TipoProduto

        fields = [
            'nmtipoproduto',
        ]

class RegistrarProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto

        fields = [
            'nmproduto',
            'precoprod',
            'fktipoprod',
        ]
class RegistrarVendaForm(forms.ModelForm):
    
    class Meta:
        model = Venda

        fields = [
            'vendedor',
            'quantidade',
        ]

class VendaForm(forms.ModelForm):
    class meta:
        model = Venda

        fields = [
            '__all__'
        ]

    def is_valid(self):
        valida = True
        if not super(dtcriacao,self).is_valid():
            self.informa_erro('O campo não pode está vazio')
            valida=False

        cat_exists = Produto.objects.filter(nome=self.data['nome']).exists()

        if(cat_exists):
            self.informa_erro('categoria já existe')
            valida=False


        return valida
    