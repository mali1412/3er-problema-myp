def saltos(l):
    """
    Dada una lista que solo contiene números enteros, cada elemento
    dentro del lista representa el tamaño máximo de un salto. Iniciando por el primer
    índice "saltamos"de tal manera que se busca determinar si es posible llegar al último
    índice.

    Parámetros:
    -----------
    l : List[int]
        Una lista de enteros donde cada valor representa el número máximo de posiciones 
        que se pueden saltar desde ese índice.

    Retorna:
    --------
    bool:
        Retorna True si es posible llegar o sobrepasar el último índice de la lista, 
        comenzando desde el índice 0. Retorna False si no es posible

    Descripción del algoritmo:
    --------------------------
    - Si la lista no contiene ningún 0, es decir, todos los saltos son posibles, la función retorna True
    - Inicializa una variable `salto_max` para mantener el valor del índice más lejano al que se puede llegar
    - Itera a través de cada índice de la lista:
        * Si el índice actual es mayor que `salto_max`, significa que no se puede llegar a ese índice,
          por lo tanto, retorna False
        * Actualiza `salto_max` 
        * Si `salto_max` es mayor o igual al último índice de la lista, retorna True.
    - Si termina el bucle y no se ha alcanzado el último índice, retorna False.
    """
     

    if 0 not in l:
        return True
    
    salto_max = 0
    
    for i in range(len(l)):
        if i > salto_max:
            return False

        salto_max = max(salto_max, i + l[i])
       
        if salto_max >= len(l) - 1:
            return True
        
    return False


