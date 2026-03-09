if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
    f = []

    for sublist in matrix:
        for item in sublist:
            f.append(item)  # Append the item to the flattened list

    print(f)

    f = [item for sublist in matrix for item in sublist]

    print(f)

    for row in matrix:
        for col in row:
            print(col)

    print([col for row in matrix for col in row])
