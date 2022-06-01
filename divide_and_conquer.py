from ast import If
import numpy as np

vector_numeros = np.array([5, 2, 4, 7, 1, 3, 2, 6])
n = vector_numeros.size

def MERGE_SORT(A, p, r):
    if (p < r):
        q = round(p + r / 2)
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q+1, r)
        MERGE(A, p, q, r)
        
def MERGE(A, p, q, r):
    if (A[p] < A[q] and A[q] < A[r]):
        pass