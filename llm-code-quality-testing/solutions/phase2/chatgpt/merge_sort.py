def merge_sort(arr):
    # Validate input is a list
    if not isinstance(arr, list):
        return False

    # Validate elements
    for x in arr:
        if x is not None and not isinstance(x, (int, float)):
            return False

    # Handle edge cases
    if len(arr) <= 1:
        return arr.copy()

    # Extract non-None values
    non_none_values = [x for x in arr if x is not None]

    # Merge sort implementation for numbers
    def merge_sort_inner(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = merge_sort_inner(lst[:mid])
        right = merge_sort_inner(lst[mid:])

        return merge(left, right)

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_values = merge_sort_inner(non_none_values)

    # Reinsert None values at original positions
    result = []
    sorted_index = 0
    for x in arr:
        if x is None:
            result.append(None)
        else:
            result.append(sorted_values[sorted_index])
            sorted_index += 1

    return result