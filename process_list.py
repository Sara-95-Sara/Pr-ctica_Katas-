from functools import reduce

def process_list(elements):
    """
    Recibe una lista de numeros y devuelve una nueva,
    con los elementos cambiados.
    Cada elemento de la nueva, sera el promedio del valor antiguo
    y el de sus vecinos
    """
    # Creo una lista vacia donde ire acumulando
    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    else:

        # por cada elemento de la lista...
       for index, element in enumerate(elements):
            # lo proceso
            new_element = process_element(index, elements)
            # lo añado a la lista
            processed_list.append(new_element)

    # devuelvo la nueva lista
    return processed_list   
    

def process_element(index, elements):
    """
    Recibe el indice de un elemento y la lista en la que esta, 
    calcula su promedio con sus vecinos
    y devuelve dicho promedio
    """
    # obtengo la lista de vecinos
    indices = get_neighbours_indices(index, elements)
    values = get_neighbours_values(indices, elements)

    # calculo su promedio
    average = get_average(values)

    # lo promedio con el elemento en si

    # devuelvo el valor final
    return average    


def get_neighbours_indices(index, elements):
    """
    Devuelve la lista de indices de los vecinos.
     Se incluye al propio elemento
    """
    indices = [] 

    indices.append(index + 1)
    indices.append(index - 1)

    # elimino los indices imposibles
    # (menores que cero y mayores o iguales a la
    # longitud de la lista)
    # Deberes : hacerle un filter a indices para eliminar valores imposibles(usando filter)
    
    indices.append(index)
    return indices    



def get_neighbours_values(indices, elements):
    values = []
    for index in indices:
        values.append(elements[index])
    return values    


def get_average(numbers):
    """
    Recibe una lista de nuemros y devuelve su promedio
    """    
    return reduce(lambda accum, b: accum + b, numbers, 0)  /  len(numbers)