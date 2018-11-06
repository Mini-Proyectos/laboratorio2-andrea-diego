import sys

def MergeSort(A:[], p: int, r: int):
	if p < r:
		q = (p+(r-1))//2
		MergeSort(A, p, q)
		MergeSort(A, q+1, r)
		Merge(A, p, q, r)
		

def Merge(A:[], p:int, q: int, r: int):
	n = q-p+1 			# tamaño de A[p...q]
	m = r-q 			# tamaño de A[q+1]
	L = [0]*(n)
	R = [0]*(m)
	for i in range(0,n):
		L[i] = A[p+i]
	for j in range(0,m):
		R[j] = A[q+j+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i, j, k = 0, 0, p
	while i<n and j<m:
		if L[i]<=R[j]:
			A[k]=L[i]	# Remover primero de L
			i = i+1
		else:
			A[k]=R[j]	# Remover primero de R
			j = j+1
		k = k+1
	while i<n:
		A[k] = L[i]
		i, k = i+1, k+1
	while j<m:
		A[k] = R[j]
		j, k = j+1, k+1

def InsertionSort(A:[], p:int, r:int):
	for j in range (p+1, r):
		key = A[j]
		i = j-1
		while i >= p and A[i]>key:
			A[i+1]=A[i]
			i = i-1
		A[i+1]=key
	return A	