import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(numbers):
    copy_random_num = numbers.copy()
    n = len(copy_random_num)
    for num in range(n):
        lowest = num
        for idx in range(num+1, n):
            if copy_random_num[idx] < copy_random_num[lowest]:
                lowest = idx
        copy_random_num[num], copy_random_num[lowest] = copy_random_num[lowest], copy_random_num[num]

    return copy_random_num


def bubble_sort(numbers):
    plt.ion()
    plt.show()
    numbers_copy = numbers.copy()
    n = len(numbers_copy)
    for num in range(n-1):
        for idx in range(n-1-num):
            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)
            if numbers_copy[num] > numbers_copy[num+1]:
                numbers_copy[num], numbers_copy[num+1] = numbers_copy[num+1], numbers_copy[num]
    plt.ioff()
    plt.show()

    return numbers_copy


def main():
    sequence = random_numbers(10, 0, 100)
    sorted1 = selection_sort(sequence)
    sorted2 = bubble_sort(sequence)
    print(sorted1)
    print(sorted2)



if __name__ == "__main__":
    main()
