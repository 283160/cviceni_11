import random

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


def main():
    sequence = random_numbers(10, 0, 100)
    sorted = selection_sort(sequence)
    print(sorted)


if __name__ == "__main__":
    main()
