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
            resultado = calculadora.calcular(form.cleaned_data)
            context = {'resultado': resultado}
    return render(request, 'index.html', context)