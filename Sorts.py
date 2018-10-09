def Mergesort(A:[], p: int, r: int):
	if p < r:
		q = (p+r)/2
		Mergesort(A, p, q)
		Mergesort(A, q+1, r)
		Merge(A, p, q, r)
		

def Merge(A:[], p:int, q: int, r: int):
	n = q-p+1			# tamaño de A[p...q]
	m = r-q				# tamaño de A[q+1]
	#Let L[1...n+1] y R[1...m+1]
	for i in range(1,n):
		L[i] = A[p+i-1]
	for i in range(1,m):
		R[i] = A[q+i]
	L[n+1] = R[m+1] # = infinito
	i, j = 1,1
	for k in range(p,r):
		if L[i]<=R[j]:
			A[k]=L[i]	# Remover primero de L
			i=i+1
		else:
			A[k]=R[j]	# Remover primero de R
			j=j+1