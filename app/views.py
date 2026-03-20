from django.http import JsonResponse
from .models import HistoricoConversao
from .services import converter_moeda

def converter_view(request):
    origem = request.GET.get('origem')
    destino = request.GET.get('destino')
    valor = float(request.GET.get('valor'))
    
    valor_convertido = converter_moeda(origem, destino, valor)
    
    HistoricoConversao.objects.create(
        moeda_origem=origem,
        moeda_destino=destino,
        valor_original=valor,
        valor_convertido=valor_convertido
    )
    
    return JsonResponse({
        "origem": origem,
        "destino": destino,
        "valor_original": valor,
        "valor_convertido": valor_convertido
    })