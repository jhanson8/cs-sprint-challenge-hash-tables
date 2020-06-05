def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    for num in weights:
        potentialMatch = limit - num
        if potentialMatch == 0.5 * limit:
            return [weights.index(num)+1, weights.index(potentialMatch)]
        if potentialMatch in cache:
            return [weights.index(num), weights.index(potentialMatch)]
        else:
            cache[num] = True 
    return None
