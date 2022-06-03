vector_numeros = [5, 2, 4, 7, 1, 3, 2, 6]
n = len(vector_numeros)

def MERGE_SORT(A, p, r):
    if (p < r):   
        
        q = round((p + r) / 2)
        left = A[p-1:q]
        right = A[q-1:r]
        left.sort()
        right.sort()
        ul = left + right
        ul.sort()
        
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q+1, r)
        MERGE(A, p, q, r)
    else:
        A.sort()
       
def MERGE(A, p, q, r):
    if (A[p] < A[q] and A[q] < A[r]):
        return A[p-1:q] + A[q:r]
        
merge_sort_call = MERGE_SORT(vector_numeros, 1, n)
print(merge_sort_call)