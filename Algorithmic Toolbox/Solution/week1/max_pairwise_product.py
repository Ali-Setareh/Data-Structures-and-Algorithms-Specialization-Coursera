import numpy as np

def max_pairwise_product(numbers):
    numbers_array = np.array(numbers)
    arg_max1 = np.argmax(numbers)
    max1=numbers[arg_max1]
    numbers_array = np.delete(numbers_array,arg_max1)
    max2 = max(numbers_array)
    return(max1*max2)

input_n = int(input())
input_numbers = [int(x) for x in input().split()]
print(max_pairwise_product(input_numbers))