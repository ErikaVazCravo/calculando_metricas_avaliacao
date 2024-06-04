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