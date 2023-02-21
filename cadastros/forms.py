from django import forms

class CalculadoraIRPFForm(forms.Form):
    vencimento_basico = forms.DecimalField(label='Informe o valor do Vencimento básico', max_digits = 10, decimal_places= 2, min_value= 0)
    incentivo_qualificacao = forms.DecimalField(label='Informe o valor do incentivo à qualificação', max_digits = 10, decimal_places= 2, min_value= 0)
    auxilio_saude = forms.DecimalField(label='Informe o valor do auxílio saúde', max_digits= 10, decimal_places= 2, min_value= 0)
    auxilio_alimentacao = forms.DecimalField(label='Informe o valor do auxílio alimentação', max_digits= 10, decimal_places= 2, min_value= 0)
    total_dependentes = forms.IntegerField(label='Informe o total de dependentes', min_value= 0)