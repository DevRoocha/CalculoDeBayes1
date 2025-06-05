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
![image](https://github.com/user-attachments/assets/76c0e1f4-1c93-4211-addb-531a83e3b9be)


------------------------------
Importa a base de dados contendo:
Prevalência de sintomas na população (dados['sintomas'])
Lista de doenças com suas probabilidades e sintomas associados (dados['doencas'])

2. Função Principal
------------------------------
![image](https://github.com/user-attachments/assets/14621418-be2c-48ea-b901-3e9a9815f444)


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
![image](https://github.com/user-attachments/assets/805c374b-49e5-4bfb-88d3-ae52cf56fe5b)


------------------------------
Calcula a probabilidade conjunta dos sintomas ocorrerem juntos na população geral

b) Cálculo para Cada Doença
------------------------------
![image](https://github.com/user-attachments/assets/b0923c3c-5c3c-4e6b-b6c7-bbc4ae1c88a8)


------------------------------
Para cada doença, inicia com sua probabilidade prévia (P(Doença))

c) Cálculo de P(Sintomas|Doença)
------------------------------
![image](https://github.com/user-attachments/assets/19295f2a-15bf-4a53-a2f4-ee3208a0c707)


------------------------------
Multiplica as probabilidades condicionais de cada sintoma dado a doença

Sintomas não listados recebem probabilidade 1% (valor arbitrário baixo)

d) Aplicação do Teorema de Bayes
------------------------------
![image](https://github.com/user-attachments/assets/a0881a6b-fac1-48f5-a157-7942b2c00734)


------------------------------
Calcula a probabilidade final da doença dados os sintomas

e) Normalização
------------------------------
![image](https://github.com/user-attachments/assets/2dba4899-c4ea-43f9-a3b2-e4aed8195025)


------------------------------
Garante que as probabilidades somem 100%


## 📊 Exemplo de Uso
------------------------------
![image](https://github.com/user-attachments/assets/b5b1738a-746c-4ac4-8e9b-21dcb4b2e8dd)

------------------------------
## Resultado Final
![image](https://github.com/user-attachments/assets/cc165fe7-be6a-4699-80b5-a017369109de)

