import sys

def MergeSort(A:[], p: int, r: int):
	if p < r:
		q = (p+r)//2
		MergeSort(A, p, q)
		MergeSort(A, q+1, r)
		Merge(A, p, q, r)
		

def Merge(A:[], p:int, q: int, r: int):
	n = q-p+1			# tamaño de A[p...q]
	m = r-q				# tamaño de A[q+1]
	L = []
	R = []
	for i in range(1,n):
		L.append(A[p+i-1])
	for i in range(1,m):
		R.append(A[q+i])
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i, j = 1,1
	for k in range(p,r):
		if L[i]<=R[j]:
			A[k]=L[i]	# Remover primero de L
			i=i+1
		else:
			A[k]=R[j]	# Remover primero de R
			j=j+1

def InsertionSort(A:[], p:int, r:int):
	for j in range (p+1, r):
		key = A[j]
		i = j-1
		while i >= p and A[i]>key:
			A[i+1]=A[i]
			i = i-1
		A[i+1]=key
	return A