import random
import time
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    """
    Sorts a list using the randomized quick sort algorithm.

    The randomized quick sort algorithm chooses a random pivot and partitions the list around it.
    All elements smaller than the pivot are on the left of the pivot, all elements larger are on the right.
    The algorithm then recursively sorts the left and right partitions.

    Args:
        arr: The list to be sorted

    Returns:
        A sorted list
    """
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    """
    Sorts a list using the deterministic quick sort algorithm.

    The deterministic quick sort algorithm chooses the middle element as the pivot and partitions the list around it.
    All elements smaller than the pivot are on the left of the pivot, all elements larger are on the right.
    The algorithm then recursively sorts the left and right partitions.

    Args:
        arr: The list to be sorted

    Returns:
        A sorted list
    """

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def measure_time(sort_func, arr, runs=5):
    """
    Measures the time taken to sort a list using a given sorting function.

    Args:
        sort_func: The sorting function to measure
        arr: The list to be sorted
        runs: The number of times to run the sorting function (default: 5)

    Returns:
        The average time taken to sort the list
    """
    
    times = []
    for _ in range(runs):
        arr_copy = list(arr)
        start = time.perf_counter()
        sort_func(arr_copy)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / runs


def main():
    sizes = [10_000, 50_000, 100_000, 500_000]
    rand_times = []
    det_times = []

    for size in sizes:
        arr = [random.randint(0, size) for _ in range(size)]
        rand_time = measure_time(randomized_quick_sort, arr)
        det_time = measure_time(deterministic_quick_sort, arr)

        rand_times.append(rand_time)
        det_times.append(det_time)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд\n")

    
    plt.figure(figsize=(8, 6))
    plt.plot(sizes, rand_times, label="Рандомізований QuickSort")
    plt.plot(sizes, det_times, label="Детермінований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
