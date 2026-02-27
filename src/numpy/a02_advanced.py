# https://www.youtube.com/watch?v=pQt8yQuPOGo
import numpy as np
import numpy.ma as ma


def example_broadcasting():
    a = np.array([1, 2, 3])  # shape:(3,)
    b = np.array([4])  # shape:(1,)
    # broadcasting happens when you have different shapes, repeating elements across axis
    print(a.shape)
    print(b.shape)
    print(a + b)  # [5 6 7] -- broadcasting to make the shapes compatible

    # shapes compatible: same size or 1 --> it can broadcast to the same shape size
    # (1,5,7,4,2) compatible with
    # (7,1,1,4,1)

    # making them compatible
    a = np.array([1, 2, 3])  # (3,)     ---> (1,3) [[1,2,3]]    ---> (2,3) [[1,2,3], [1,2,3]]
    b = np.array([[4], [5]])  # (2,1)   ---> (2,1)->(2,3)       ---> (2,3) [4,4,4], [5,5,5]


def advanced_indexing():
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
    print(a[0][1])  # 2
    print(a[0:2])  # first 2 rows: [[1 2 3] [4 5 6]]
    print(a[(0, 2)])  # using tuple, 3 element
    print(a[[0, 2]])  # using list, 0+2. row
    print(a[:, :])  # everything
    print("\n", a[:, 1])  # row=everything, column=1. = [2 5 8]
    #     masking
    print(a[[[True, False, False], [True, False, True],
             [True, False, True]]])  # [1 4 6 7 9] - masking which elements are shown


def sorting_example():
    a = np.array([[5, 8, 3],
                  [4, 9, 6],
                  ])
    print(np.sort(a))
    print(np.sort(a, axis=0))  # vertical sort
    print(np.sort(a.flatten()).reshape(a.shape))  # sort from low to high


def search_example():
    outputs = np.array([0.65, 0.34, 0.28, 0.84, 0.1, 0, 0.56, 0.03])
    print(np.argmax(outputs))  # index of max value
    print(np.argmin(outputs))  # index of min value
    print(np.argmin([0.65, 0.01, 0.28, 0.84, 0.1, 0.01, 0.56, 0.01]))  # first match
    print(np.nonzero(outputs))
    print(np.where(outputs >= 0.5))


def iteration_example():
    a = np.arange(24).reshape(3, 4, 2)
    print(a)

    for row in a:
        for middlerow in row:
            for element in middlerow:
                print(element, end=' ')
    print()

    for element in np.nditer(a, order='F'):
        print(element, end=' ')
    print()

    with np.nditer(a, op_flags=['readwrite']) as it:
        for element in it:
            element[...] = element ** 2
    print(a)


def masking_example():
    arr = np.array([1, 2, 3, np.nan, 4, np.inf])
    # sorting - I dont want to use them (some values) at calculation but dont want to remove them from the list
    masked_arr = ma.masked_array(arr, mask=[0, 0, 0, 1, 0, 1])
    print(masked_arr)
    print(masked_arr.mean())
    print(masked_arr.sum())
    print(ma.getmask(masked_arr))
    print(ma.masked_greater(arr, 2))
    print(ma.masked_inside(arr, 1, 2))
    print(ma.masked_outside(arr, 1, 2))
    print(ma.masked_invalid(arr))
    a = np.array([1, 2, 3, 4, 5])
    print(ma.masked_where(a % 2 == 0, a))


def view_copy_example():
    # view = new viewpoint to the same data
    arr = np.array([1, 2, 3, 4, 5])
    new_arr = arr[0:3]  # view
    print(new_arr)


if __name__ == '__main__':
    # example_broadcasting()
    # advanced_indexing()
    # sorting_example()
    # search_example()
    # iteration_example()
    # masking_example()
    view_copy_example()
