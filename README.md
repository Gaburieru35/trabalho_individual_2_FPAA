# MaxMin Select - Algoritmo de Seleção Simultânea do Maior e do Menor Elementos

## Descrição do Projeto

Este projeto implementa o algoritmo **MaxMin Select** utilizando a abordagem de **divisão e conquista** para encontrar o maior e o menor elemento em uma sequência de números. O objetivo é reduzir o número de comparações em relação à abordagem ingênua, tornando o algoritmo mais eficiente.

O algoritmo funciona dividindo a lista em sublistas menores recursivamente, encontrando os valores mínimo e máximo em cada sublista e combinando os resultados.

## Como executar o projeto

### Pré-requisitos

- Python 3.x instalado

### Passos para execução

1. Clone este repositório:
   ```sh
   git clone https://github.com/Gaburieru35/trabalho_individual_2_FPAA.git
   ```
2. Acesse a pasta do projeto:

3. Execute o script Python:
   ```sh
   python main.py
   ```

## Explicação do Algoritmo

O algoritmo **MaxMin Select** segue os seguintes passos:

1. Se o array possuir apenas um elemento, este é tanto o mínimo quanto o máximo.
2. Se houver dois elementos, a comparação direta determina o menor e o maior.
3. Se houver mais elementos:
   - Divide-se o array em duas metades.
   - Aplica-se a recursão em cada metade para obter os valores mínimos e máximos.
   - Os valores finais são obtidos comparando os mínimos e os máximos de cada metade.

**Código principal:**

```python
def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[left]  # Caso base: um único elemento
    
    if right - left == 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)
```

## Análise da Complexidade

### Contagem de Operações

O número de comparações realizadas pelo algoritmo segue a recorrência:

```math
T(n) = 2T(n/2) + O(1)
```

A cada nível da recursão, há **2 chamadas recursivas** e **duas comparações adicionais** para combinar os resultados.
A resolução dessa recorrência leva a um número total de comparações de aproximadamente **3n/2 - 2**, resultando em complexidade **O(n)**.

### Aplicação do Teorema Mestre

A recorrência pode ser analisada pelo **Teorema Mestre**, onde:

- **a = 2** (número de chamadas recursivas)
- **b = 2** (tamanho da divisão)
- **f(n) = O(1)** (custo da combinação)

Calculamos:

```math
log_b(a) = log_2(2) = 1
```

O caso correspondente no Teorema Mestre é **O(n^p)**, onde **p = 1**, resultando em **O(n)**.

## Conclusão

O algoritmo **MaxMin Select** é eficiente para encontrar os extremos de um conjunto de números, reduzindo as comparações necessárias em comparação com métodos ingênuos. Sua complexidade O(n) garante bom desempenho mesmo para grandes volumes de dados.

## Autor

Gabriel Henrique Mota Rodrigues
