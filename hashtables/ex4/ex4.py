def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    negative_nums = []
    positive_nums = []

    for num in range(len(a)):
        cache[num] = a[num]
        if cache[num] < 0:
            negatives = cache[num]
            negative_nums.append(negatives)
        if cache[num] > 0:
            positives = cache[num]
            positive_nums.append(positives)
        for n in negative_nums:
            for p in positive_nums:
                if abs(n) == p & p not in result:
                    result.append(p)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
