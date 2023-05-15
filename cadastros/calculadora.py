from . models import AliquotaCSS, AliquotaIRPF, TabelaIRPF
from datetime import date
from django.db.models import Max
from decimal import Decimal

# contribuição previdenciária por alíquota

ZERO = 0
PERCENTUAL = Decimal(1) / Decimal(100)

def calcular(dados):
    # contribuição para seguridade social
    css_a_pagar = ZERO
    vencimento_basico = dados.get('vencimento_basico')
    incentivo_qualificacao = dados.get('incentivo_qualificacao')
    rendimento_tributavel = vencimento_basico + incentivo_qualificacao
    valor_remanescente = rendimento_tributavel
    # obtem as aliquotas css
    ano_atual = date.today().year
    aliquotas_css = AliquotaCSS.objects.filter(tabela_css__ano_vigencia=str(ano_atual)).order_by('aliquota')
    for object in aliquotas_css:
        if rendimento_tributavel > object.valor_final:
            valor_remanescente = rendimento_tributavel - object.valor_final
            css_a_pagar += (object.valor_final - object.valor_inicial) * object.aliquota * PERCENTUAL
        else:
            css_a_pagar += valor_remanescente * object.aliquota * PERCENTUAL
            break
    print(f'Valor da contribuição à seguridade social: {css_a_pagar:.2f}')
    # obtem as aliquotas irpf
    irpf_a_pagar = ZERO
    aliquotas_irpf = AliquotaIRPF.objects.filter(tabela_irpf__ano_vigencia=str(ano_atual)).order_by('aliquota')
    tabela_irpf = TabelaIRPF.objects.get(ano_vigencia=str(ano_atual))
    total_dependentes = dados.get('total_dependentes')
    if not total_dependentes:
        total_dependentes = Decimal(ZERO)
    deducao_dependente = total_dependentes * tabela_irpf.deducao_dependente_mes
    base_calculo = rendimento_tributavel - css_a_pagar - deducao_dependente
    valor_remanescente = base_calculo
    maior_aliquota = aliquotas_irpf.aggregate(Max('aliquota')).get('aliquota__max')
    for object in aliquotas_irpf:
        if base_calculo > object.valor_final and object.aliquota != maior_aliquota:
            valor_remanescente = base_calculo - object.valor_final
            irpf_a_pagar += (object.valor_final - object.valor_inicial) * object.aliquota * PERCENTUAL
        else:
            irpf_a_pagar += valor_remanescente * object.aliquota * PERCENTUAL
            break

    print(f'Valor do IRPf: {irpf_a_pagar:.2f}')

    contribuicao_sindical = rendimento_tributavel * PERCENTUAL
    auxilio_alimentacao = dados.get('auxilio_alimentacao')
    auxilio_saude = dados.get('auxilio_saude')
    rendimento_nao_tributavel = auxilio_alimentacao + auxilio_saude
    descontos = css_a_pagar + irpf_a_pagar + contribuicao_sindical
    salario_liquido = rendimento_tributavel + rendimento_nao_tributavel - descontos

    print(f'Valor do salário líquido: {salario_liquido:.2f}')

    resultado = {
        'rendimento_tributavel': round(rendimento_tributavel, 2),
        'rendimento_nao_tributavel': round(rendimento_nao_tributavel, 2),
        'css_a_pagar': round(css_a_pagar, 2),
        'irpf_a_pagar': round(irpf_a_pagar, 2),
        'salario_liquido': round(salario_liquido, 2),
        'total_dependentes': dados.get('total_dependentes')
    }

    return resultado