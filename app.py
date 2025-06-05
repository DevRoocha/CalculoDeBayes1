import json
from data.doencas import dados

def calcular_probabilidades(sintomas_selecionados):
    # Pega as informações das doenças
    doencas = dados['doencas']
    total_pacientes = dados['total_pacientes']
    
    resultados = {}
    explicacao = []
    
    # Calcula P(Sintomas) - probabilidade conjunta dos sintomas
    p_sintomas = 1.0
    for sintoma in sintomas_selecionados:
        p_sintoma = dados['sintomas'][sintoma]['probabilidade']
        p_sintomas *= p_sintoma
    
    # Para cada doença, calcula P(Doença|Sintomas)
    for doenca in doencas:
        # P(Doença) - probabilidade a priori
        p_doenca = doenca['probabilidade']
        
        # P(Sintomas|Doença) - produto das probabilidades dos sintomas dada a doença
        p_sintomas_dado_doenca = 1.0
        explicacao_doenca = []
        
        for sintoma in sintomas_selecionados:
            if sintoma in doenca['sintomas']:
                p = doenca['sintomas'][sintoma]
            else:
                # Se o sintoma não está associado à doença, usamos uma probabilidade pequena
                p = 0.01
                
            p_sintomas_dado_doenca *= p
            explicacao_doenca.append(f"P({sintoma}|{doenca['nome']}) = {p:.2f}")
        
        # Teorema de Bayes
        p_doenca_dado_sintomas = (p_doenca * p_sintomas_dado_doenca) / p_sintomas
        
        # Normaliza para porcentagem (0-100)
        p_doenca_dado_sintomas *= 100
        
        resultados[doenca['nome']] = p_doenca_dado_sintomas
        
        # Prepara explicação detalhada
        explicacao.append(
            f"Para {doenca['nome']}: P(D)={p_doenca:.4f}, " +
            " × ".join(explicacao_doenca) +
            f" → P(D|S) = {p_doenca_dado_sintomas:.2f}%"
        )
    
    # Normaliza os resultados para que a soma seja 100%
    total = sum(resultados.values())
    if total > 0:
        for doenca in resultados:
            resultados[doenca] = (resultados[doenca] / total) * 100
    
    return resultados, explicacao