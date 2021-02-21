import numpy as np

UPPER_BOUNDARY = 100  # boundaries of sort
LOWER_BOUNDARY = -UPPER_BOUNDARY
ADD_RANGE = 10  # max length of arrays is n plus ADD_RANGE


def create_array(len, n):
    """Create arrays with random values
    Args:
        len(numpy.ndarray): arrays lengths
        n(int): number of arrays

    """
    arr = [0] * n
    for i in range(n):
        arr[i] = np.random.uniform(LOWER_BOUNDARY, UPPER_BOUNDARY, len[i])
    return arr


def array_sort(arr, n):
    """Sort even arrays in ascending order (0,2,4...)
            odd arrays in descending order (1,3,5...)
    Args:
        arr(list): arrays
        n(int): number of arrays

    """
    for i in range(n):
        if i % 2 == 0:
            arr[i].sort()
        else:
            arr[i][::-1].sort()


def function(n):
    array_lengths = np.random.permutation(n+ADD_RANGE)[:n]  # generate unique lengths
    arr = create_array(array_lengths, n)
    array_sort(arr, n)
    return arr


n = int(input("Enter n: "))
for i in function(n):
    print(i)
    print("|||||||||||||||||||||||||||")
