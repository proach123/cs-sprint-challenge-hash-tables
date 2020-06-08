def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    first = None
    second = None

    for i in range(len(weights)):
        if (weights[i] not in cache) and (limit - weights[i] in weights):
            cache[weights[i]] = i
            if __name__ == "__main__":
                print(cache[weights[i]])
    



    if len(cache) == 2:

        for weight in cache:
            if first == None:
                first = cache[weight]
            else:
                second = cache[weight]

        if first > second:
            return (first, second)
        else: return (second, first)


    elif len(cache) == 1:
        for i in range(len(weights)):
            if weights[i] in cache:
                if first == None:
                    first = i
                else: second = i
        
        if first > second:
            return (first,second)
        else: return (second, first)


    return None





if __name__ == "__main__":
    print(get_indices_of_item_weights([9], 1, 9))
    print(get_indices_of_item_weights([9,5,6,7], 1, 20))
    print(get_indices_of_item_weights([4,4], 2, 8))
    print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
    

# # Merging Two Packages

# Given a package with a weight limit `limit` and a list `weights` of item
# weights, implement a function `get_indices_of_item_weights` that finds
# two items whose sum of weights equals the weight limit `limit`. Your
# function will return an instance of an `Answer` tuple that has the
# following form:

# ```
# (zero, one)
# ```

# where each element represents the item weights of the two packages.
# _**The higher valued index should be placed in the `zeroth` index and
# the smaller index should be placed in the `first` index.**_ If such a
# pair doesn’t exist for the given inputs, your function should return
# `None`.

# Your solution should run in linear time.

# Example:
# ```
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21
# ```

# ## Hints
 
# * A brute-force solution would involve two nested loops, yielding a
#   quadratic-runtime solution. How can we use a hash table in order to
#   implement a solution with a better runtime?

# * Think about what we can store in the hash table in order to help us to
#   solve this problem more efficiently. 

# * What if we store each weight in the input list as keys? What would be
#   a useful thing to store as the value for each key? 

# * If we store each weight's list index as its value, we can then check
#   to see if the hash table contains an entry for `limit - weight`. If it
#   does, then we've found the two items whose weights sum up to the
#   `limit`!