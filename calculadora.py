# contribuição previdenciária por alíquota

css_aliquota = {
    7.5: [0, 1302.01],
    9.0: [1302.01, 2571.29],
    12.0: [2571.30, 3856.94],
    14.0: [3856.95, 7507.49],
    14.5: [7507.50, 12856.50],
    16.5: [12856.51, 25712.99],
    19.0: [25713.00, 50140.33],
    22.0: [50140.34, 50140.34]
}

irpf_aliquota = {
    0: [0, 1903.98],
    7.5: [1903.99, 2826.65],
    15.0: [2826.66, 3751.05],
    22.5: [3751.06, 4664.68],
    27.5: [4664.69, 4664.69],
}

salario = int(input('Entre com o salário: '))
# contribuição para seguridade social
css_a_pagar = 0

valor_remanescente = salario

for key, value in css_aliquota.items():
    if salario > value[1]:
        valor_remanescente = salario - value[1]
        css_a_pagar += (value[1] - value[0]) * key / 100
    else:
        css_a_pagar += valor_remanescente * key / 100
        break

print(css_a_pagar)

# irpf
deducao_dependente = 3 * 189.59
irpf_a_pagar = 0
base_calculo = salario - css_a_pagar - deducao_dependente
valor_remanescente = base_calculo

for key, value in irpf_aliquota.items():
    if base_calculo > value[1] and key != 27.5:
        valor_remanescente = base_calculo - value[1]
        irpf_a_pagar += (value[1] - value[0]) * key / 100
    else:
        irpf_a_pagar += valor_remanescente * key / 100
        break

print(irpf_a_pagar)

auxilio_saude = 439
auxilio_alimentacao = 458
contribuicao_sindical = salario * 1 / 100

salario_liquido = salario - css_a_pagar - irpf_a_pagar  - contribuicao_sindical + auxilio_saude + auxilio_alimentacao

print(salario_liquido)
