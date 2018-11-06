import Sorts
import sys
import time
from random import randint

inicio = time.time()
algoritmo = str(sys.argv[1])
n = int(sys.argv[2])
i = 0
A = []
while i!=n:
	A.append(randint(0,1000))
	i = i+1
if algoritmo == "MergeSort":
	Sorts.MergeSort(A, 0, n-1)
else:
	Sorts.InsertionSort(A, 0, n)
fin = time.time()
tiempo = (fin-inicio) * 1000
print(algoritmo, n, str(tiempo))