def hvg_vector(vector):
    mult = 1
    hvg = 0

    for element in vector:
        if element > 0:
            mult *= element
            hvg = round(mult ** (1 / len(vector)))
        else:
            return -1
    return hvg

def find_elements_vector_above_avg(vector, hvg):
    count = 0

    for element in vector:
        if element > hvg:
            count += 1
    return count

def find_elements_vector_below_avg(vector, hvg):
    count = 0

    for element in vector:
        if element < hvg:
            count += 1
    return count

def find_nearest_element_to_hvg(vector, d_discrepancy, hvg):
    ls = []
    count = 0
    for j in range(hvg - d_discrepancy, hvg + d_discrepancy + 1):
        for element in vector:
            if element == j:
                count += 1
                ls.append(element)
    return (count, ls)