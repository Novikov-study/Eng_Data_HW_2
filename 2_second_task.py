import numpy as np
import  os

matrix = np.load(r"./data/second_task.npy")
x = []
y = []
z = []

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        if matrix[i][j] > 586:
            x.append(i)
            y.append(j)
            z.append(matrix[i][j])

np.savez("second_task_result.npz", x=x, y=y, z=z)
#print(np.load("second_task.npz"))

np.savez_compressed("second_task_result_compress.npz", x=x, y=y, z=z)

first_size = os.path.getsize('second_task_result.npz')
second_size = os.path.getsize('second_task_result_compress.npz')

print(f"savez = {first_size}")
print(f"savez_compressed = {second_size}")
print(f"diff = {first_size - second_size}")