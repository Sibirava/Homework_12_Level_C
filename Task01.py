def avg_vector(vector):
    sum = 0
    avg = 0

    for element in vector:
        sum += element
        avg = round(sum / len(vector))
    return avg

def find_elements_vector_above_avg(vector, avg):
    count = 0

    for element in vector:
        if element > avg:
            count += 1
    return count

def find_elements_vector_below_avg(vector, avg):
    count = 0

    for element in vector:
        if element < avg:
            count += 1
    return count

def find_nearest_element_to_avg(vector, d_discrepancy, avg):
    ls = []
    count = 0
    for j in range(avg - d_discrepancy, avg + d_discrepancy + 1):
        for element in vector:
            if element == j:
                count += 1
                ls.append(element)
    return (count, ls)
