from django.db import models

class TipoUsuario (models.Model):
    desc = models.CharField(max_length=50)

    def __str__(self):
        return self.desc

class Usuario (models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=9)
    tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.PROTECT)

    def __str__(self):
        return "{nome} {cpf}"

class Planta (models.Model):
    tipo_planta = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    nome = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.nome

class PedidoCarrinho (models.Model):
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade_itens = models.IntegerField()

class ItensCarrinho (models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT,)
    pedido = models.ForeignKey(PedidoCarrinho, on_delete=models.PROTECT)
    dt_entrega = models.DateField()
    dth = models.DateTimeField()
    endereco = models.CharField(max_length=200)

class Curtida (models.Model):
    dth = models.DateTimeField()
    qnt_curtida = models.IntegerField()
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)





