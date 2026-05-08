def merge_sort(arr):
    if not isinstance(arr, list):
        return False
    for x in arr:
        if not isinstance(x, (int, float, type(None))):
            return False

    def compare(a, b):
        if a is None and b is None:
            return True
        if a is None:
            return True
        if b is None:
            return False
        return a <= b

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if compare(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_recursive(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr[:]
        mid = len(sub_arr) // 2
        left = merge_sort_recursive(sub_arr[:mid])
        right = merge_sort_recursive(sub_arr[mid:])
        return merge(left, right)

    return merge_sort_recursive(arr)