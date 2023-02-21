from django.shortcuts import render, redirect
from . forms import CalculadoraIRPFForm
from . import calculadora

# Create your views here.

def index(request):
    if request.method == 'GET':
        form = CalculadoraIRPFForm()
        context = {'form': form}
    else:
        form = CalculadoraIRPFForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            dados = {
                'vencimento_basico': request.POST.get('vencimento_basico'),
                'incentivo_qualificacao': request.POST.get('incentivo_qualificacao'),
                'auxilio_saude': request.POST.get('auxilio_saude'),
                'auxilio_alimentacao': request.POST.get('auxilio_alimentacao'),
                'total_dependentes': request.POST.get('total_dependentes'),
            }
            resultado = calculadora.calcular(dados)
            context = {'resultado': resultado}
    return render(request, 'index.html', context)