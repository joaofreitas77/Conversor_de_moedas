from django.db import models

# Create your models here.

class HistoricoConversao(models.Model):
    moeda_origem = models.CharField(max_length=3);
    moeda_destino = models.CharField(max_length=3);
    valor_original = models.DecimalField(max_digits=5 ,decimal_places=2);
    valor_convertido = models.DecimalField(max_digits=5, decimal_places=2);
    data_conversao = models.DateTimeField(auto_now_add = True);
