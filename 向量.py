import timeit
import numpy as np

# 定义测试数据生成函数
def generate_test_data(size):
    return np.random.randint(1, 100, size=size)

# 平凡算法
def sum_of_numbers_trivial(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 超标量优化算法
def sum_of_numbers_optimized(numbers):
    while len(numbers) > 1:
        new_numbers = []
        for i in range(0, len(numbers)-1, 2):
            new_numbers.append(numbers[i] + numbers[i+1])
        if len(numbers) % 2 == 1:
            new_numbers.append(numbers[-1])
        numbers = new_numbers
    return numbers[0]

# 测试程序
if __name__ == "__main__":
    sizes = [1000, 10000, 100000]  # 不同问题规模
    num_repeats = 10  # 每个问题规模的重复次数

    for size in sizes:
        print(f"Problem Size: {size}")
        numbers = generate_test_data(size)

        # 测试平凡算法
        trivial_time = timeit.timeit(lambda: sum_of_numbers_trivial(numbers), number=num_repeats)
        print("Trivial Algorithm Time (average):", trivial_time / num_repeats)

        # 测试优化算法
        optimized_time = timeit.timeit(lambda: sum_of_numbers_optimized(numbers), number=num_repeats)
        print("Optimized Algorithm Time (average):", optimized_time / num_repeats)

        print()  # 添加空行以便区分不同问题规模
