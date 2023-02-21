from django.db import models

# contribuição à seguridade social  
class TabelaCSS(models.Model):
    class Meta:
        verbose_name = 'Tabela de contribuição à seguridade social'
        verbose_name_plural = 'Tabelas de contribuição à seguridade social'
    
    ano_vigencia = models.CharField(verbose_name='Ano de Vigência', max_length=4)

    def __str__(self):
        return f'Tabela CCS vigente em {self.ano_vigencia}'

class AliquotaCSS(models.Model):

    class Meta:
        verbose_name = 'Alíquota de contribuição à seguridade social'
        verbose_name_plural = 'Alíquotas de contribuição à seguridade social'

    aliquota = models.DecimalField(verbose_name='Alíquota', max_digits=10, decimal_places=2)
    valor_inicial = models.DecimalField(verbose_name='Valor Inicial', max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(verbose_name='Valor Final', max_digits=10, decimal_places=2)
    tabela_css = models.ForeignKey(TabelaCSS, verbose_name='Tabela CSS', on_delete=models.CASCADE)

    def __str__(self):
        return f'Alíquota {self.aliquota:.2f}%'

# imposto de renda pessoa física
class TabelaIRPF(models.Model):
    class Meta:
        verbose_name = 'Tabela do imposto de renda'
        verbose_name_plural = 'Tabelas do imposto de renda'
    
    ano_vigencia = models.CharField(verbose_name='Ano de Vigência', max_length=4)
    deducao_dependente_mes = models.DecimalField(verbose_name='Desconto mensal por dependente', max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Tabela IRPF vigente em {self.ano_vigencia}'
    
class AliquotaIRPF(models.Model):
    class Meta:
        verbose_name = 'Alíquota do imposto de renda'
        verbose_name_plural = 'Alíquotas do imposto de renda'
    
    aliquota = models.DecimalField(verbose_name='Alíquota', max_digits=10, decimal_places=2)
    valor_inicial = models.DecimalField(verbose_name='Valor Inicial', max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(verbose_name='Valor Final', max_digits=10, decimal_places=2)
    tabela_irpf = models.ForeignKey(TabelaIRPF, verbose_name='Tabela IRPF', on_delete=models.CASCADE)

    def __str__(self):
        return f'Alíquota {self.aliquota:.2f}%'