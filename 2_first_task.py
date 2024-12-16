import json
import numpy as np


matrix = np.load("./data/first_task.npy")

size = matrix.size # общее число элементов

matrix_props = {
    'sum': 0,
    'avr': 0,
    'sumMD': 0,  #главная
    'avrMD': 0,  #главная
    'sumSD': 0,  #побочная
    'avrSD': 0,  #побочная
    'max': matrix[0][0],
    'min': matrix[0][0]
}

for i in range (matrix.shape[0]): #строки
    for j in range (matrix.shape[1]): #столбцы
        el = matrix[i][j]  #позиция
        matrix_props['sum'] += el
        if i == j:
            matrix_props['sumMD'] += el
        if j == matrix.shape[1] - i - 1:
            matrix_props['sumSD'] += el

        if matrix_props['max'] < el:  #обновляем максимум
            matrix_props['max'] = el
        if matrix_props['min'] > el:  #обновляем минимум
            matrix_props['min'] = el
# средние
matrix_props['avr'] = matrix_props['sum']/ size
matrix_props['avrMD'] = matrix_props['sumMD']/ matrix.shape[0]
matrix_props['avrSD'] = matrix_props['sumSD']/ matrix.shape[1]

for key in matrix_props.keys():
    matrix_props[key] = float(matrix_props[key]) # преобразуем все ключи

with open ("first_task_result.json" , "w", encoding="utf-8") as f:
    json.dump(matrix_props, f)

norm_matrix = matrix / matrix_props['sum']
np.save("first_task_result_np.npy", norm_matrix)

print(np.load("first_task_result_np.npy").sum()) #должно быть близко к 1.0