def selection_sort(arr):
    n = len(arr)

    # Loop over each position in the list
    for i in range(n):
        # Assume the current position has the smallest element
        min_index = i

        # Look through the rest of the list to find the true smallest
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest found with the current position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the sorted list
    return arr
