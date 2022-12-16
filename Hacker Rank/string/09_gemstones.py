def gemstones(arr):
    result = set(arr[0])

    for i in range(1, len(arr)):
        temp = set(arr[i])

        result = result.intersection(temp)

    return len(result)
