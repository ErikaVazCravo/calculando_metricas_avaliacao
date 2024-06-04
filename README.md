# Desafios de Código - Simulando Desafios com IAs Generativas
# 5 / 5 - Calculando Métricas de Avaliação

## Desafio

Você faz parte de uma equipe que está desenvolvendo modelos de Machine Learning para identificar a probabilidade de inadimplência em empréstimos concedidos por uma instituição financeira. Após treinar os modelos, sua tarefa é avaliar seu desempenho usando algumas métricas de avaliação. Nesse contexto, o desafio é criar um algoritmo que receba n matrizes de confusão e retorne o índice, precisão e acurácia da matriz que apresenta o melhor desempenho com base no cálculo dessas métricas. Lembrando que:

- Acurácia é calculada pela fórmula: (VP + VN) / (VP + FP + FN + VN)
- Precisão é calculada pela fórmula: VP / (VP + FP)

Onde:

- VP (Verdadeiro Positivo): Casos em que o modelo previu corretamente a classe positiva.
- FP (Falso Positivo ou Erro Tipo I): Casos em que o modelo previu incorretamente a classe positiva.
- FN (Falso Negativo ou Erro Tipo II): Casos em que o modelo previu incorretamente a classe negativa.
- VN (Verdadeiro Negativo): Casos em que o modelo previu corretamente a classe negativa.

### Entrada:

A entrada consiste em uma string composta por: n, representando o número de matrizes de confusão, seguido dos valores que compõem as n matrizes.

Cada matriz consiste em quatro valores, onde os dois primeiros representam a primeira linha da matriz, composta por verdadeiros positivos (VP) e falsos positivos (FP); os dois últimos valores representam a segunda linha, que é composta por falsos negativos (FN) e verdadeiros negativos (VN). As duas linhas e os valores que as compõem estão separados por vírgulas.

### Saída:

O resultado esperado inclui o valor do índice, acurácia e precisão (arredondada para duas casas decimais) da matriz com melhor desempenho com base no cálculo dessas métricas.

### Exemplos

A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| Entrada | Saída |
|---------|-------|
| 3<br>50,10,5,85<br>20,5,8,67<br>30,12,4,88 | Índice: 1<br>Acurácia: 0.9<br>Precisão: 0.83 |
| 4<br>70,15,8,78<br>60,20,10,80<br>45,5,3,92<br>80,7,15,98 | Índice: 3<br>Acurácia: 0.94<br>Precisão: 0.9 |
| 2<br>100,0,0,50<br>80,10,2,98 | Índice: 1<br>Acurácia: 1.0<br>Precisão: 1.0 |

#### Atenção:

Se você não está familiarizado com a linguagem de programação, não se preocupe! Você pode usar uma das seguintes inteligências artificiais para te ajudar a entender o código:

- [ChatGPT](https://chat.openai.com/)
- [Copilot](https://copilot.microsoft.com/)
- [Gemini](https://gemini.google.com/)
- [Amazon Q (Para Empresas)](https://aws.amazon.com/pt/q/)

Abaixo adicionamos algumas sugestões e uso e Prompts para te auxiliar na resolução:

| Sugestões de Uso | Sugestões de Prompts |
|------------------|----------------------|
| Explicação de Conceitos | Pode me explicar o que são estruturas de dados e dar exemplos? |
| Entendimento do Problema | Quais são as restrições ou requisitos específicos que devo considerar neste desafio? |
| Sugestões de Abordagem | Quais são as etapas principais que devo seguir para resolver este desafio? |
| Ajuda na Depuração | Estou recebendo um erro de sintaxe neste trecho de código. O que pode estar errado? |
| Revisão de Algoritmos | Você pode revisar meu algoritmo de ordenação e me dar feedback sobre sua eficiência? |

# SOLUÇÃO COMENTADA:

    def calculate_metrics(matrix):
        # Extrair valores da matriz de confusão
        vp, fp, fn, vn = map(int, matrix)
    
        # Calcular acurácia
        accuracy = (vp + vn) / (vp + fp + fn + vn)
    
        # Calcular precisão
        if vp + fp != 0:
            precision = vp / (vp + fp)
        else:
            precision = 0  # Lidando com divisão por zero
    
        return accuracy, precision
    
    def best_performance(matrices):
        best_index = 0
        best_accuracy = 0
        best_precision = 0
        
        for index, matrix in enumerate(matrices):
            # Calcular métricas para a matriz atual
            accuracy, precision = calculate_metrics(matrix)
    
            # Verificar se as métricas atuais são melhores do que as melhores métricas encontradas até agora
            if (accuracy + precision) > (best_accuracy + best_precision):
                best_index = index + 1
                best_accuracy = accuracy
                best_precision = precision
    
        return best_index, best_accuracy, best_precision
    
    def format_number(number):
        # Se o número for um inteiro, adiciona .0
        if number.is_integer():
            return f"{number:.1f}"
        # Caso contrário, remove a segunda casa decimal se for zero
        return f"{number:.2f}".rstrip('0').rstrip('.')
    
    n = int(input())
    matrices = []
    
    for n in range(0,n):
        matrix = input().split(',')
        matrices.append(matrix)
    
    best_index, best_accuracy, best_precision = best_performance(matrices)
    
    print(f"Índice: {best_index}")
    print(f"Acurácia: {format_number(best_accuracy)}")
    print(f"Precisão: {format_number(best_precision)}")
    
