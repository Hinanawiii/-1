import timeit
import numpy as np


def generate_test_data(size):
    matrix = np.random.randint(1, 100, size=(size, size))
    vector = np.random.randint(1, 100, size=size)
    return matrix, vector


def column_vector_inner_product_no_loop(matrix, vector):
    result = np.dot(matrix.T, vector)
    return result.tolist()


if __name__ == "__main__":
    sizes = [100, 500, 1000]  
    num_repeats = 10 

    for size in sizes:
        print(f"Problem Size: {size}")
        matrix, vector = generate_test_data(size)

        
        no_loop_time = timeit.timeit(lambda: column_vector_inner_product_no_loop(matrix, vector), number=num_repeats)
        print("No Loop Algorithm Time (average):", no_loop_time / num_repeats)

        print()  
