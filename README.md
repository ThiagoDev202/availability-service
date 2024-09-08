# Calculadora de Disponibilidade de Serviço em Múltiplos Servidores

Este projeto aborda o cálculo da **disponibilidade** de um serviço replicado em múltiplos servidores. Em um cenário de sistemas distribuídos, é comum utilizar múltiplos servidores para garantir a **resiliência** e **alta disponibilidade** de um serviço. No entanto, a probabilidade de o serviço estar disponível varia conforme o número de servidores, a probabilidade de cada servidor estar ativo e o número mínimo de servidores necessários para atender a uma requisição.

## Problema

Queremos calcular a **disponibilidade** de um serviço com base em três parâmetros principais:

- **n**: Número total de servidores disponíveis no sistema.
- **k**: Número mínimo de servidores necessários para o serviço funcionar.
- **p**: Probabilidade de cada servidor estar disponível.

As operações do serviço podem ser classificadas em três categorias:

1. **Consulta (k = 1)**: O serviço é acessível se pelo menos um servidor estiver disponível.
2. **Atualização (k = n)**: Todos os servidores precisam estar disponíveis.
3. **Caso Geral (1 < k < n)**: Pelo menos `k` servidores precisam estar disponíveis.

O objetivo é desenvolver um método eficiente que calcule a disponibilidade para esses três cenários com base nos parâmetros fornecidos.

## Solução

A solução está implementada na classe `AvailabilityCalculator`, que calcula a disponibilidade do serviço de acordo com os parâmetros fornecidos. A seguir estão os componentes principais do código:

### Classe `AvailabilityCalculator`

Esta classe realiza o cálculo da disponibilidade do serviço replicado. Ela possui três métodos principais para calcular a disponibilidade em diferentes cenários:

- **_availability_for_query**: Calcula a disponibilidade para operações de consulta (`k = 1`).
- **_availability_for_update**: Calcula a disponibilidade para operações de atualização (`k = n`).
- **_general_availability**: Calcula a disponibilidade para o caso geral, onde `1 < k < n`.

A função **calculate_availability** determina qual método usar com base no valor de **k** e retorna a disponibilidade calculada.

## Gráfico de Disponibilidade

![Gráfico de Disponibilidade](https://drive.google.com/uc?export=view&id=1legi2tVNjYVo26LbvLvVHH-afLLIcjiT)

O eixo **X** representa o número mínimo de servidores necessários (**k**) para que o serviço esteja disponível.  
O eixo **Y** representa a **disponibilidade** calculada do serviço, variando de 0 a 1.  

Cada linha colorida no gráfico representa um valor de **n**, o número total de servidores no sistema. Por exemplo:  

- A linha **azul** mostra o caso em que há **n = 1** servidor, onde a disponibilidade diminui conforme a probabilidade de disponibilidade do único servidor cai.  
- A linha **laranja** mostra o caso com **n = 3** servidores e como a disponibilidade varia com o aumento do número de servidores necessários para operar.

À medida que o valor de **n** aumenta, a disponibilidade permanece alta para valores menores de **k**, mas pode diminuir drasticamente quando mais servidores são exigidos.  
O gráfico ilustra que aumentar o número total de servidores (**n**) geralmente melhora a disponibilidade, mas a disponibilidade diminui drasticamente se o número de servidores necessários (**k**) for muito próximo de **n**.
