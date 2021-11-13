# M FERDY HASAN
# 202010225204
# TF3A4

# Interpolasi Lagrange
import numpy as np

# membaca jumlah titik data
n = int(input('Masukan jumlah titik data : '))

# membuat array ukuran n x n dan inisiasi
x = np.zeros((n))
y = np.zeros((n))

# membaca titik data
print('Masukan data x dan y : ')
for i in range(n):
    x[i] = float(input('x['+str(i)+'] = '))
    y[i] = float(input('y['+str(i)+'] = '))

# membaca interpolasi titik
xp = float(input('Masukan x yang diinginkan : '))

# inisiasi interpolasi
yp = 0

# implementasi interpolasi lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p*(xp - x[j])/(x[i] - x[j])
        yp = yp + p * y[i]

# display output
print('Nilai interpolasi untuk %.3f adalah %.3f.' % (xp, yp))