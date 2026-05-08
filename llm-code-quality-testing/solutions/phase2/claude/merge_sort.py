def merge_sort(arr):
    if not isinstance(arr, list):
        return False

    for element in arr:
        if element is not None and not isinstance(element, (int, float)):
            return False

    if len(arr) <= 1:
        return arr.copy()

    non_none = [x for x in arr if x is not None]
    none_count = arr.count(None)

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

    def sort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = sort(lst[:mid])
        right = sort(lst[mid:])
        return merge(left, right)

    sorted_non_none = sort(non_none)
    return sorted_non_none + [None] * none_count

