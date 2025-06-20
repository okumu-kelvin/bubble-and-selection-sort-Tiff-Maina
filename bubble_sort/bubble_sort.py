def bubble_sort(unsorted_list):
    n = len(unsorted_list)

    # Loop through the list multiple times
    for i in range(n):
        # In each pass, compare adjacent elements up to the unsorted part
        for j in range(0, n - i - 1):
            # If the left element is greater than the right, swap them
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]

    # Return the sorted list
    return unsorted_list
