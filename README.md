# Tia Lu Delivery

A Tia Lu Delivery é um app da empresa foodDelivery que está sendo construído por nossas equipes.

Este repositório tem como objetivo a primeira atividade da área de dados, que consiste na construção de uma biblioteca de estatística em Python.


## Estrutura da Classe Statistics

A classe Statistics foi implementada para manipular datasets estruturados como dicionários (dict[str, list]), onde cada chave representa o nome de uma coluna e o valor é uma lista de dados.

* Validação de dados
   * Confere se o dataset é um dicionário.
   * Garante que todas as colunas tenham o mesmo tamanho.
   * Verifica se colunas numéricas contêm apenas números.
* Medidas de Tendência Central
    * mean(column) → Média aritmética
    * median(column) → Mediana
    * mode(column) → Moda (suporta múltiplas modas)
* Medidas de Dispersão
    * variance(column) → Variância populacional
    * stdev(column) → Desvio padrão populacional
* Associação Entre Variáveis
    * covariance(column_a, column_b) → Covariância
* Frequências
    * itemset(column) → Itens únicos
    * absolute_frequency(column) → Frequência absoluta
    * relative_frequency(column) → Frequência relativa
    * cumulative_frequency(column, frequency_method) → Frequência acumulada (absoluta ou relativa)
* Probabilidade
   * conditional_probability(column, value1, value2) → Probabilidade condicional


## Exemplo de Uso

```python

# Exemplo de dataset
dataset = {
    "vendas": [10, 20, 20, 30, 40, 50],
    "clientes": [1, 2, 3, 4, 5, 6]
}

# Criando objeto da classe
stats = Statistics(dataset)

# Usando métodos
print(stats.mean("vendas"))  
print(stats.median("vendas")) 
print(stats.mode("vendas"))  
print(stats.stdev("vendas"))  

```
##  Estrutura do Repositório

```text
Tia-Lu-Delivery
┣ 📜 statistics.py             
┣ 📜 tests.py                  
┣ 📜 README.md                 
┣ 📄 apresentacao_vitoria.pdf  
┗ 📄 relatorio_tecnico_vitoria.pdf  

```

##  Testes
O projeto conta com testes automatizados para validar cada função da biblioteca.

Execute os testes com:

```text
python -m unittest tests.py
```


