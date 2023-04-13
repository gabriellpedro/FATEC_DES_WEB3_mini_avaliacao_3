from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from core.models import FeriadoModel


def verifica_feriado(request):
    qs = FeriadoModel.objects.all()
    data_atual = date.today()
    feriado_nome = 'Hoje não é nenhum feriado... Que pena :('
    for feriado in qs:
        if(feriado.dia == data_atual.day and feriado.mes == data_atual.month):
            feriado_nome = feriado.nome
    contexto = {
        'feriado' : feriado_nome
    } 
    return render(request, 'feriado.html', contexto)
       