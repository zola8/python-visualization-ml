import numpy as np


# https://www.youtube.com/watch?v=4c_mwnYdbhQ

def example1():
    global a
    a = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[2, 3, 4], [5, 6, 7]]])
    print(a)
    print(a[1][0])
    print(a.shape)  # (2, 2, 3)
    print(a.ndim)  # 3 = number of dimension
    print(a.size)  # 12, number of elements
    print(a.dtype)  # int64 = data type

    print(np.array([1, "abc", 3]).dtype)  # <U21, string less than 21 chars, each element is string now


def example2():
    print(np.full((3, 4), 8))
    print()
    print(np.empty((2, 4)))  # allocate memory but not initialized
    print(np.zeros((2, 4)))
    print()
    print(np.arange(0, 100, 5))  # with step size
    print(np.linspace(0, 100, 5))  # how many values we have in this range
    print(np.nan)
    print(np.nan * np.nan)
    print(np.inf)
    print(np.inf * np.nan)


def example3():
    normal_list = [1, 2, 3]
    np_arr = np.array([1, 2, 3])
    print(normal_list * 2)
    print(np_arr * 2)


def example4():
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.delete(a, 0))  # first element
    print(np.delete(a, 0, 0))  # first row
    print(np.delete(a, 1, 0))  # second row
    print(np.delete(a, 0, 1))  # first column


def example5():
    a = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15],
                  [16, 17, 18, 19, 20]])
    print(a.shape)
    print(a.reshape(2, 10))
    print(a.reshape(5, 2, 2))  # 5 collections with 2 lists each with 2 elements each
    print(a.flatten())
    print(a.transpose())  # swap rows with cols
    # np.save("numbers.npy", a)
    # np.savetxt('numbers.csv', a, delimiter=',', fmt='%d')


if __name__ == '__main__':
    # example1()
    # example2()
    # example3()
    # example4()
    example5()
