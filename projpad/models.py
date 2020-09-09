from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.utils import timezone


class TipoProduto(models.Model):
	nmtipoproduto = models.CharField(max_length=50)
	def __str__(self):
		return f'{self.nmtipoproduto}'
	
class TipoCargo(models.Model):
	nmtipocargo = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
	def __str__(self):
		return self.nmtipocargo

class Produto(models.Model):
	nmproduto = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
	precoprod = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
	fktipoprod = models.ForeignKey(TipoProduto, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.nmproduto}'



class Funcionario(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    cpf = models.CharField(
        max_length = 255,
        null = False,
        blank= False
    )
    remuneracao = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False
    )
    fkcargo =  models.ForeignKey(TipoCargo, on_delete=models.CASCADE)

class Venda(models.Model):

	vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

	quantidade = models.FloatField()

	dtcriacao = models.DateTimeField(editable=False)
	dtmodificacao = models.DateTimeField(editable=False)

	def save(self, *args, **kwargs):
	    ''' On save, update timestamps '''
	    if not self.id:
	    	self.dtcriacao = timezone.now()
	    self.dtmodificacao = timezone.now()

	def __str__(self):
		return  'Venda '+ str(self.id) +' vendedor '+ str(self.vendedor)

class Venda_Produto(models.Model):
    fkvenda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    fkproduto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.fkvenda) +' prod. '+ str(self.fkproduto)


objects = models.Manager()