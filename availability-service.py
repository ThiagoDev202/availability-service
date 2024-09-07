import math
from typing import Union

class AvailabilityCalculator:
    def __init__(self, n: int, k: int, p: float):
        """
        Inicializa o cálculo da disponibilidade.
        
        :param n: Número total de servidores (n > 0)
        :param k: Número mínimo de servidores disponíveis (0 < k ≤ n)
        :param p: Probabilidade de um servidor estar disponível (0 ≤ p ≤ 1)
        """
        self.n = n
        self.k = k
        self.p = p

    def calculate_availability(self) -> Union[float, None]:
        """
        Calcula a disponibilidade do serviço replicado com base no número de servidores
        e no número mínimo de servidores disponíveis necessários.
        
        :return: Disponibilidade do serviço (0 ≤ disponibilidade ≤ 1)
        """
        if self.k == 1:
            return self._availability_for_query()
        elif self.k == self.n:
            return self._availability_for_update()
        elif 1 < self.k < self.n:
            return self._general_availability()
        else:
            raise ValueError("Valores de k e n inválidos. Certifique-se de que 0 < k ≤ n.")

    def _availability_for_query(self) -> float:
        """
        Calcula a disponibilidade no caso de operação de consulta (k = 1),
        ou seja, quando pelo menos 1 servidor deve estar disponível.
        
        :return: Disponibilidade do serviço
        """
        return 1 - (1 - self.p) ** self.n

    def _availability_for_update(self) -> float:
        """
        Calcula a disponibilidade no caso de operação de atualização (k = n),
        ou seja, quando todos os servidores devem estar disponíveis.
        
        :return: Disponibilidade do serviço
        """
        return self.p ** self.n

    def _general_availability(self) -> float:
        """
        Calcula a disponibilidade para o caso geral, onde k servidores devem estar disponíveis.
        
        :return: Disponibilidade do serviço
        """
        # Soma binomial para calcular a disponibilidade quando k servidores ou mais devem estar disponíveis
        availability = sum(
            self._binomial_coefficient(self.n, i) * (self.p ** i) * ((1 - self.p) ** (self.n - i))
            for i in range(self.k, self.n + 1)
        )
        return availability

    @staticmethod
    def _binomial_coefficient(n: int, k: int) -> int:
        """
        Calcula o coeficiente binomial "n choose k", ou seja, C(n, k) = n! / (k! * (n - k)!)
        
        :param n: Número total de elementos
        :param k: Número de elementos a serem escolhidos
        :return: Valor do coeficiente binomial
        """
        return math.comb(n, k)

# Exemplo de uso:
if __name__ == "__main__":
    # Parâmetros
    n = 5  # Número de servidores
    k = 3  # Número mínimo de servidores necessários
    p = 0.9  # Probabilidade de cada servidor estar disponível

    calculator = AvailabilityCalculator(n, k, p)
    disponibilidade = calculator.calculate_availability()

    print(f"Disponibilidade do serviço: {disponibilidade:.4f}")


# Resposta:
# Com 5 servidores e a necessidade de ter pelo menos 3 disponíveis para o serviço funcionar,
# e considerando que cada servidor tem uma probabilidade de 90% de estar disponível,
# a disponibilidade geral do serviço é alta, atingindo 99,14%.
# Isso significa que, na maior parte do tempo, o serviço estará disponível,
# pois a probabilidade de falha simultânea de mais de 2 servidores é baixa.