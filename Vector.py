import random
NUMBER = 10
RANDOM_VALUE_UP = 100
RANDOM_VALUE_DOWN = 1
def random_vector_elements():
    n = NUMBER
    vector = [random.randint(RANDOM_VALUE_DOWN, RANDOM_VALUE_UP) for i in range(n)]
    return vector
