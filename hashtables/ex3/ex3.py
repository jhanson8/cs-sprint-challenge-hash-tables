def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result =[]
    for array in arrays:
        for num in array:
            if num in cache:
                cache[num] += 1
                # result.append(num)
            else:
                cache[num] = 1
    for values in cache:
        if cache[values] > 1:
            result.append(values)
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
