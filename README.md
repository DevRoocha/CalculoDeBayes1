# Documentação do Sistema de Diagnóstico Médico Bayesiano

## 📌 Visão Geral
Este projeto implementa um sistema de diagnóstico médico probabilístico usando o Teorema de Bayes. O sistema calcula a probabilidade de diversas doenças com base nos sintomas selecionados pelo usuário, utilizando dados estatísticos de prevalência de doenças e sintomas.

## 🔍  Teorema de Bayes
O sistema utiliza a fórmula:
P(Doença|Sintomas) = [P(Doença) × P(Sintomas|Doença)] / P(Sintomas)

Onde:

P(Doença): Probabilidade prévia da doença na população

P(Sintomas|Doença): Probabilidade dos sintomas dado que o paciente tem a doença

P(Sintomas): Probabilidade geral dos sintomas na população

## 🧠 Lógica de Implementação
1. Entrada de Dados

------------------------------
![image](https://github.com/user-attachments/assets/c5801755-608f-4c1f-add5-bda80ab9aab6)

------------------------------
Importa a base de dados contendo:
Prevalência de sintomas na população (dados['sintomas'])
Lista de doenças com suas probabilidades e sintomas associados (dados['doencas'])

2. Função Principal
------------------------------
![image](https://github.com/user-attachments/assets/60a150e8-8a58-4d65-9b78-68d0e73d708c)

------------------------------
Parâmetro:

sintomas_selecionados: Lista de strings com os nomes dos sintomas selecionados

Retorno:

Tupla (resultados, explicacao) onde:

resultados: Dicionário {doença: probabilidade}

explicacao: Lista de strings com detalhes dos cálculos

3. Passo a Passo do Algoritmo
a) Cálculo de P(Sintomas)
------------------------------
![image](https://github.com/user-attachments/assets/075cbea4-771c-408e-b174-f14d88b0938c)

------------------------------
Calcula a probabilidade conjunta dos sintomas ocorrerem juntos na população geral

b) Cálculo para Cada Doença
------------------------------
![image](https://github.com/user-attachments/assets/855e22fd-fa89-4ce8-9f1e-65cac8240044)

------------------------------
Para cada doença, inicia com sua probabilidade prévia (P(Doença))

c) Cálculo de P(Sintomas|Doença)
------------------------------
![image](https://github.com/user-attachments/assets/9eeb62cb-6ce9-472f-a3ba-526682dcaa3f)

------------------------------
Multiplica as probabilidades condicionais de cada sintoma dado a doença

Sintomas não listados recebem probabilidade 1% (valor arbitrário baixo)

d) Aplicação do Teorema de Bayes
------------------------------
![image](https://github.com/user-attachments/assets/1fc4c0ab-191b-473d-a952-13a3534a8412)

------------------------------
Calcula a probabilidade final da doença dados os sintomas

e) Normalização
------------------------------
![image](https://github.com/user-attachments/assets/3b76aa76-aab1-43a7-95d4-b0d076cb17b1)

------------------------------
Garante que as probabilidades somem 100%


## 📊 Exemplo de Uso
------------------------------
![image](https://github.com/user-attachments/assets/b5b1738a-746c-4ac4-8e9b-21dcb4b2e8dd)

------------------------------
