from django.shortcuts import render
from .models import HistoricoConversao
from .services import converter_moeda

def converter_view(request):
    origem = request.GET.get('origem')
    destino = request.GET.get('destino')
    valor = request.GET.get('valor')
    
    envia_dados = {}
    
    if origem and destino and valor:
        valor = float(valor)
    
        valor_convertido = converter_moeda(origem, destino, valor)
    
        HistoricoConversao.objects.create(
            moeda_origem=origem,
            moeda_destino=destino,
            valor_original=valor,
            valor_convertido=valor_convertido
        )
    
        envia_dados = {
            "origem": origem,
            "destino": destino,
            "valor_original": valor,
            "valor_convertido": valor_convertido
        }
    
    return render(request, "converter.html", envia_dados)