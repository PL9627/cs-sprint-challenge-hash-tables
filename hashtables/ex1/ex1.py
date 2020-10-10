def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    store = {}

    for i, weight in enumerate(weights):
        store[weight] = i

    for i, weight in enumerate(weights):
        if limit - weight in store:
            j = store[limit - weight]
            
            if i > j:
                return (i, j)
            else:
                return(j, i)
    
    return None
