def merge_sort(arr):
    if not isinstance(arr, list):
        return False

    # Extract non-None values and validate types
    items_to_sort = []
    none_indices = []

    for i, val in enumerate(arr):
        if val is None:
            none_indices.append(i)
        elif isinstance(val, (int, float)):
            items_to_sort.append(val)
        else:
            return False

    def sort_logic(data):
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        left = sort_logic(data[:mid])
        right = sort_logic(data[mid:])

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

    sorted_numbers = sort_logic(items_to_sort)

    # Reconstruct list preserving None positions
    final_list = [None] * len(arr)
    num_idx = 0
    none_set = set(none_indices)

    for i in range(len(arr)):
        if i not in none_set:
            final_list[i] = sorted_numbers[num_idx]
            num_idx += 1

    return final_list