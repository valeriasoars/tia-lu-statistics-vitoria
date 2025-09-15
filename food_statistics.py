class Statistics:
    """
    Uma classe para realizar cálculos estatísticos em um conjunto de dados.

    Atributos
    ----------
    dataset : dict[str, list]
        O conjunto de dados, estruturado como um dicionário onde as chaves
        são os nomes das colunas e os valores são listas com os dados.
    """
    def __init__(self, dataset):
        """
        Inicializa o objeto Statistics.

        Parâmetros
        ----------
        dataset : dict[str, list]
            O conjunto de dados, onde as chaves representam os nomes das
            colunas e os valores são as listas de dados correspondentes.
        """
        if not isinstance(dataset, dict):
            raise TypeError("O dataset deve ser um dicionário.")
        
        for value in dataset.values():
            if not isinstance(value, list):
               raise TypeError("Todos os valores no dicionário do dataset devem ser listas.") 
        
        #talvez essa condição seja desnecessária
        if dataset:
            sizes = [len(value) for value in dataset.values()]
            #eu acho que poderia ser uma condição vendo o tamanho de um conjunto, seria mais fácil
            if not all(size == sizes[0] for size in sizes):
                raise ValueError("Todas as colunas no dataset devem ter o mesmo tamanho.")
            
        self.dataset = dataset

    #gosto de termos esse método
    def _validate_column(self, column):
        if column not in self.dataset: 
            raise KeyError(f"A coluna '{column}' não existe no dataset")
        #eu acho que aqui vocês poderia ter feito uma validação para 
        #ver se o conjunto não estava vazio
        #você poderiam ter lançado uma exceção
    
    def _validade_numeric_column(self, column):
        self._validate_column(column)
        data = self.dataset[column]

        if data == []:
            return #empty response pode ser problemático em algumas métricas
        
        #essa validação é fundamental para várias das métricas
        #vocês poderiam ter escrito-as como: 
        #if not all(isinstance(value, (int, float)) for value in data):
        for value in data: 
            if not isinstance(value, (int, float)):
                raise TypeError(f"A coluna '{column}' deve ter apenas valores numéricos")

    def mean(self, column):
        """
        Calcula a média aritmética de uma coluna.

        Fórmula:
        $$ \mu = \frac{1}{N} \sum_{i=1}^{N} x_i $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A média dos valores na coluna.
        """
        self._validade_numeric_column(column)
        data = self.dataset[column]

        #eu não sei se retornar zero seja o melhor nesse caso, mas entendo por causa dos testes
        if data == []:
            return 0.0
        
        #muito bom, mas poderia colocar o retorno na mesma linha
        mean = sum(data) / len(data)
        #return sum(data)/len(data)
        return mean

    def median(self, column):
        """
        Calcula a mediana de uma coluna.

        A mediana é o valor central de um conjunto de dados ordenado.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O valor da mediana da coluna.
        """
        #validação muito bem feita aqui, afinal a mediana é uma 
        #métrica de tendência central com dados numéricos. 

        self._validade_numeric_column(column)
        data = self.dataset[column]
        sorted_data = sorted(data) #muito bem por terem usado os 
        #a ordenação com o sorted e não com o .sort, pois assim
        #geramos uma cópia dos dados

        size = len(sorted_data)

        if size < 1: return 0.0 #isso aqui não é muito bom
        #não temos uma indentação correta
        # aqui a condição poderia ter sido: 

        #a verificação do tamanho poderia ter sido feita antes 
        #da ordenação 
        # if len(data) == 0 

        if size%2 == 0:
            #aqui vocês poderiam ter removido a definição do índice 
            #middle_index = size // 2 
            # (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
            return (sorted_data[size//2 - 1] + sorted_data[size//2]) / 2
        
        return sorted_data[size//2]

    def mode(self, column):
        """
        Encontra a moda (ou modas) de uma coluna.

        A moda é o valor que aparece com mais frequência no conjunto de dados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        list
            Uma lista contendo o(s) valor(es) da moda.
        """
        #a moda é a única das métricas de tendência central que 
        #funciona bem com dados categóricos, ou seja, a moda 
        #funciona para dados não numéricos. 
        self._validate_column(column)
        data = self.dataset[column]

        #eu prefiro a verificação com o tamanho (len -> 0)
        if data == []:
            return []
        

        # aqui era para termos um reuso da métrica de freq absoluta
        frequencia = {}

        mode = []

        for value in data:
            if value not in frequencia: 
                frequencia[value] = 0
            frequencia[value] += 1
        
        #a metrica começaria daqui
        frequenciaMax = max(frequencia.values())
        
        #vocês poderia reescrever essa linha da seguinte forma:
        #mode = [i for i, j in frequencia.items() if j == frequenciaMax]

        for i, j in frequencia.items():
            if j == frequenciaMax: 
                mode.append(i)
        return mode

    def stdev(self, column):
        """
        Calcula o desvio padrão populacional de uma coluna.

        Fórmula:
        $$ \sigma = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            O desvio padrão dos valores na coluna.
        """
        self._validade_numeric_column(column)
        data = self.dataset[column]

        #aqui você poderia ter chamado a variância
        mean = self.mean(column) #aqui um reuso do código 
        #muito bom

        sum = 0.0

        #essa condição deveria estar antes de calcular a média 
        #complicado
        if data == []: return 0.0

        #aqui você poderia ter chamado a variância
        for x in data:
            sum += (x - mean) ** 2
        
        variance = sum / len(data)

        stdev = variance ** 0.5

        #esse método todo poderia ser
        #return self.variance(column=column) ** 0.5 
        
        return stdev



    def variance(self, column):
        """
        Calcula a variância populacional de uma coluna.

        Fórmula:
        $$ \sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N} $$

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        float
            A variância dos valores na coluna.
        """
        self._validade_numeric_column(column)
        data = self.dataset[column]

        #eu acho que essa validação deveria estar um pouquinho antes
        if data == []:
            return 0.0
        
        mean_value = self.mean(column)
        #mean_value = sum(data)/len(data)
        squared_diffs = [(x - mean_value) ** 2 for x in data]
        #poderia colocar o return direto
        variance = sum(squared_diffs) / len(data)
        return variance

    def covariance(self, column_a, column_b):
        """
        Calcula a covariância entre duas colunas.

        Fórmula:
        $$ \text{cov}(X, Y) = \frac{\sum_{i=1}^{N} (x_i - \mu_x)(y_i - \mu_y)}{N} $$

        Parâmetros
        ----------
        column_a : str
            O nome da primeira coluna (X).
        column_b : str
            O nome da segunda coluna (Y).

        Retorno
        -------
        float
            O valor da covariância entre as duas colunas.
        """
        desvio_a = []
        desvio_b = []
        ListaDesvios = []

        self._validade_numeric_column(column_a)
        data_a = self.dataset[column_a]

        self._validade_numeric_column(column_b)
        data_b = self.dataset[column_b]

        if data_a == [] or data_b == []:
            return 0.0
        
        mean_value_a = self.mean(column_a)
        mean_value_b = self.mean(column_b)
        #mean_value = sum(data)/len(data)

        #aqui seria mais idiomático
        #ListaDesvios = [(data_a - mean_value_a) * (data_b - mean_value_b) for data_a, data_b in zip(data_a, data_b)]


        for value in data_a:
            desvio_a.append(value - mean_value_a)
        for value in data_b:
            desvio_b.append(value - mean_value_b)
        
        
        for i in range(len(data_a)):
            desvioCorrespondente = desvio_a[i] * desvio_b[i]
            ListaDesvios.append(desvioCorrespondente)
        
        #aqui poderia colocar direto no return 
        #return sum(ListaDesvios) / len(data_a)
        covariance = sum(ListaDesvios) / len(data_a)
        
        return covariance


    def itemset(self, column):
        """
        Retorna o conjunto de itens únicos em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        set
            Um conjunto com os valores únicos da coluna.
        """
        self._validate_column(column)
        data = self.dataset[column]
        #aqui você poderia já ter colocado o return 
        #return set(data)
        itemset = set(data)
        return itemset

    def absolute_frequency(self, column):
        """
        Calcula a frequência absoluta de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas contagens (frequência absoluta).
        """
        self._validate_column(column)
        data = self.dataset[column]

        if data == []:
            return {}
        
        absolute_frequency = {}

        for value in data:
            if value not in absolute_frequency: 
                absolute_frequency[value] = 0
            absolute_frequency[value] += 1

        return absolute_frequency

    def relative_frequency(self, column):
        """
        Calcula a frequência relativa de cada item em uma coluna.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).

        Retorno
        -------
        dict
            Um dicionário onde as chaves são os itens e os valores são
            suas proporções (frequência relativa).
        """
        #aqui o ideal era ter chamado o método de freq absoluta no inicio 
        #frequencia_absoluta = self.absolute_frequency(column=column)
        #ele já faria essa validações

        self._validate_column(column)
        data = self.dataset[column]

        if data == []:
            return {}
        
        #aqui o ideal era ter chamado o método de freq absoluta antes de tudo
        frequencia_absoluta = {}
        frequencia_relativa = {}

        for value in data:
            if value not in frequencia_absoluta: 
                frequencia_absoluta[value] = 0
            frequencia_absoluta[value] += 1
    
            
        totalFrequencias = sum(frequencia_absoluta.values())

        for value in frequencia_absoluta:
            frequencia_relativa[value] = frequencia_absoluta[value] / totalFrequencias

        #aqui poderia ser simplificado
        #return [frequencia_absoluta[value]/totalFrequencias for value in frequencia_absoluta]

        return frequencia_relativa 


    def cumulative_frequency(self, column, frequency_method='absolute'):
        """
        Calcula a frequência acumulada (absoluta ou relativa) de uma coluna.

        A frequência é calculada sobre os itens ordenados.

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        frequency_method : str, opcional
            O método a ser usado: 'absolute' para contagem acumulada ou
            'relative' para proporção acumulada (padrão é 'absolute').

        Retorno
        -------
        dict
            Um dicionário ordenado com os itens como chaves e suas
            frequências acumuladas como valores.
        """

        #aqui foi muito ruim a implementação dessa forma, pois você já tem os 
        # métodos para calcular a freq absoluta e relativa
        frequencia_absoluta = {}
        frequencia_acumulada_absoluta = {}
        frequencia_acumulada_relativa = {}

        self._validate_column(column)
        data = self.dataset[column]

        data.sort() # isso é ruim, pois se você ordena a coluna e muda a ordem 
        #dos dados no dataset original 

        for value in data:
            if value not in frequencia_absoluta: 
                frequencia_absoluta[value] = 0
            frequencia_absoluta[value] += 1

        acumulador = 0

        #esse cara deveria tá depois de computar a frequência
        for value in frequencia_absoluta:
            acumulador += frequencia_absoluta[value]
            frequencia_acumulada_absoluta[value] = acumulador 
            frequencia_acumulada_relativa[value] = acumulador / len(data)
        
        #esses ifs deveria estar no inicio, chamando os métodos
        if frequency_method == "absolute":
            return frequencia_acumulada_absoluta
        elif frequency_method == "relative":
            return frequencia_acumulada_relativa
        else:
            raise ValueError("O 'frequency_method' deve ser 'absolute' ou 'relative'.")


    def conditional_probability(self, column, value1, value2):
        """
        Calcula a probabilidade condicional P(X_i = value1 | X_{i-1} = value2).

        Este método trata a coluna como uma sequência e calcula a probabilidade
        de encontrar `value1` imediatamente após `value2`.

        Fórmula: P(A|B) = Contagem de sequências (B, A) / Contagem total de B

        Parâmetros
        ----------
        column : str
            O nome da coluna (chave do dicionário do dataset).
        value1 : any
            O valor do evento consequente (A).
        value2 : any
            O valor do evento condicionante (B).

        Retorno
        -------
        float
            A probabilidade condicional, um valor entre 0 e 1.
        """
        self._validade_numeric_column(column)
        data = self.dataset[column]

        if len(data) < 2:
            return 0.0
        
        count_value2 = data.count(value2)

        if count_value2 == 0:
            return 0.0 
        
        sequence_count = 0
        for i in range(len(data) - 1):
            if data[i] == value2 and data[i + 1] == value1:
                sequence_count += 1

        #achei que foi positivo
        conditional_probability = sequence_count / count_value2
        return conditional_probability
    