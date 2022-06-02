vector_numeros = [5, 2, 4, 7, 1, 3, 2, 6]
n = len(vector_numeros)

def MERGE_SORT(A, p, r):
    if (p < r):
        new_vector = []
        for i in range(p-1, r):
            new_vector.append(A[i])
        new_vector.sort()
        vector_numeros.clear()
        for number in new_vector:
            vector_numeros.append(number)
            
        q = round(p + r / 2)
        MERGE_SORT(A, p, q)
        MERGE_SORT(A, q+1, r)
        MERGE(A, p, q, r)
        
    """    restas_elements = []
        restas_elements.append(aux - element)
        curr_vector = []
        rest_aux = 0
        for rest in restas_elements:
            rest_aux += rest
            if (restas_elements.index(rest) == 0):
                continue
            else:
                if (rest_aux - rest <= rest):
                    rest_aux = rest_aux - (rest_aux - rest)
                    mayor = rest_aux
                    restas_elements.append(mayor)
                    index = restas_elements.index(mayor)
                    curr_vector.append(A[index])
                else:
                    rest_aux = rest_aux - rest
                    mayor = rest_aux
                    restas_elements.append(mayor)
                    index = restas_elements.index(mayor)
                    curr_vector.append(A[index])
                    
                outer = []
                for list_item in curr_vector:
                    outer.append(list_item)
                    vector_numeros = np.array(outer)
                        
                sorted = vector_numeros
                return sorted
    """
        
def MERGE(A, p, q, r):
    if (A[p] < A[q] and A[q] < A[r]):
        left
        for l in range(p-1, q):
            left = A[l]
            
        right
        for r in range(q, r):
            right = A[r]
        print(left + right)
        """new_arr1 = A[p:q+1]
        new_arr2 = A[q+1: r+1]
        vector_numeros =  np.concatenate((new_arr1, new_arr2))
    return vector_numeros
    """
        
MERGE_SORT(vector_numeros, 1, n)