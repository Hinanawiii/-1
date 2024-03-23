import timeit
import numpy as np

# 定义测试数据生成函数
def generate_test_data(size):
    matrix = np.random.randint(1, 100, size=(size, size))
    vector = np.random.randint(1, 100, size=size)
    return matrix, vector

# 平凡算法
def column_vector_inner_product_trivial(matrix, vector):
    result = []
    for col in range(len(matrix[0])):
        dot_product = sum(matrix[row][col] * vector[row] for row in range(len(matrix)))
        result.append(dot_product)
    return result

# 超标量优化算法
def column_vector_inner_product_optimized(matrix, vector):
    result = []
    for col in range(len(matrix[0])):
        dot_product = sum(matrix[row][col] * vector[row] for row in range(len(matrix)))
        result.append(dot_product)
    return result

# 测试程序
if __name__ == "__main__":
    sizes = [100, 500, 1000]  # 不同问题规模
    num_repeats = 10  # 每个问题规模的重复次数

    for size in sizes:
        print(f"Problem Size: {size}")
        matrix, vector = generate_test_data(size)

        # 测试平凡算法
        trivial_time = timeit.timeit(lambda: column_vector_inner_product_trivial(matrix, vector), number=num_repeats)
        print("Trivial Algorithm Time (average):", trivial_time / num_repeats)

        # 测试优化算法
        optimized_time = timeit.timeit(lambda: column_vector_inner_product_optimized(matrix, vector), number=num_repeats)
        print("Optimized Algorithm Time (average):", optimized_time / num_repeats)

        print()  # 添加空行以便区分不同问题规模
