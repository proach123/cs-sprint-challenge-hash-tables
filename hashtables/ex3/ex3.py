def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for i in arrays:
        for j in i:
            if j not in cache:
                cache[j] = 1
            else:
                cache[j] += 1
    
    for key,v in cache.items():
        if v > 1:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

# # Intersections of Multiple Lists

# Find the intersection between multiple lists of integers.

# Do not use numpy or sets to solve this; use `dict` or hashtables,
# please.

# We're given a list of lists that contain integers:

# ```python
# [
#     [1, 2, 3, 4, 5],
#     [12, 7, 2, 9, 1],
#     [99, 2, 7, 1,]
# ]
# ```

# And we need to compute the _intersection_, that is, numbers that exist
# in all lists.

# From the above input, the return value will be:

# ```
# [1, 2]
# ```

# Because those are the numbers that exist in all the lists.

# (Output can be in any order.)

# Limits:

# * There can be up to 10 lists in the list of lists.
# * The lists can contain up to roughly 1,000,000 elements each.
