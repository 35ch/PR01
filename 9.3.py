n = list(map(int, input("Please provide to numbers separated by a space: ").split()))

def maximum(numbers):
    numbers.sort()
    print(f"{numbers[1]} is the biggest number!")

maximum(n)

