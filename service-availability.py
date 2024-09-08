import math
import pandas as pd
import matplotlib.pyplot as plt

class AvailabilityCalculator:
    """
    Classe responsável por calcular a disponibilidade de um serviço replicado em múltiplos servidores.
    O cálculo pode ser feito para três cenários: 
    - Consulta (k=1), 
    - Atualização (k=n),
    - Caso geral (1 < k < n).
    """
    def __init__(self, n: int, k: int, p: float):
        """
        Inicializa a classe com os parâmetros:
        n: número de servidores,
        k: número mínimo de servidores necessários para o serviço ser acessado,
        p: probabilidade de cada servidor estar disponível.
        """
        self.n = n
        self.k = k
        self.p = p

    def _binomial_coefficient(self, n: int, k: int) -> int:
        """
        Calcula o coeficiente binomial C(n, k), que é o número de combinações possíveis
        de k itens escolhidos de um conjunto de n itens. Utilizado para calcular a disponibilidade
        no caso geral (1 < k < n).
        """
        return math.comb(n, k)

    def _availability_for_query(self) -> float:
        """
        Calcula a disponibilidade do serviço no caso de uma operação de consulta, onde
        k = 1. Aqui, o serviço está disponível se pelo menos um servidor estiver disponível.
        """
        return 1 - (1 - self.p) ** self.n

    def _availability_for_update(self) -> float:
        """
        Calcula a disponibilidade do serviço no caso de uma operação de atualização, onde
        k = n. Aqui, o serviço está disponível apenas se todos os servidores estiverem disponíveis.
        """
        return self.p ** self.n

    def _general_availability(self) -> float:
        """
        Calcula a disponibilidade do serviço para o caso geral, onde 1 < k < n.
        Utiliza o coeficiente binomial para somar as probabilidades de pelo menos k servidores
        estarem disponíveis.
        """
        total_probability = 0
        for i in range(self.k, self.n + 1):
            total_probability += (
                self._binomial_coefficient(self.n, i)
                * (self.p ** i)
                * ((1 - self.p) ** (self.n - i))
            )
        return total_probability

    def calculate_availability(self) -> float:
        """
        Método principal que calcula a disponibilidade com base no valor de k:
        - Se k = 1, chama _availability_for_query(),
        - Se k = n, chama _availability_for_update(),
        - Caso contrário, chama _general_availability() para o caso geral.
        """
        if self.k == 1:
            return self._availability_for_query()
        elif self.k == self.n:
            return self._availability_for_update()
        else:
            return self._general_availability()

# Função para testar diferentes valores de n, k e p
def test_availability():
    """
    Define uma lista de valores de n, k e p para testar. Para cada combinação desses valores,
    calcula a disponibilidade utilizando a classe AvailabilityCalculator e organiza os resultados
    em um DataFrame. Por fim, exibe a tabela e plota os gráficos.
    """
    # Definindo os valores de n, k e p para teste
    test_values = [
        (1, 1, 0.9),  # Caso base, sem replicação
        (3, 1, 0.9),
        (3, 2, 0.9),
        (3, 3, 0.9),
        (5, 1, 0.9),
        (5, 3, 0.9),
        (5, 5, 0.9),
        (10, 5, 0.95),
        (10, 7, 0.95),
        (10, 10, 0.95),
        (20, 10, 0.99),
        (20, 15, 0.99),
        (20, 20, 0.99)
    ]

    results = []

    # Calculando a disponibilidade para cada combinação de n, k e p
    for n, k, p in test_values:
        calculator = AvailabilityCalculator(n, k, p)
        availability = calculator.calculate_availability()
        results.append({"n": n, "k": k, "p": p, "availability": availability})

    # Organizando os resultados em um DataFrame
    df = pd.DataFrame(results)
    
    # Exibindo a tabela
    print(df)

    # Plotando os gráficos
    plot_availability(df)

# Função para plotar os resultados
def plot_availability(df: pd.DataFrame):
    """
    Plota gráficos 2D mostrando a relação entre o número mínimo de servidores disponíveis (k)
    e a disponibilidade do serviço para diferentes valores de n (número total de servidores).
    """
    fig, ax = plt.subplots()

    # Agrupa os dados por n e plota a disponibilidade para diferentes valores de k
    for key, grp in df.groupby('n'):
        ax.plot(grp['k'], grp['availability'], label=f'n={key}', marker='o')

    # Configurando o título e os rótulos dos eixos
    plt.title('Disponibilidade do Serviço para Diferentes Valores de n e k')
    plt.xlabel('k (Número Mínimo de Servidores Necessários)')
    plt.ylabel('Disponibilidade')
    plt.legend(title='n (Número de Servidores)')
    plt.grid(True)
    plt.show()

# Executando o teste e visualizando os resultados
test_availability()
