def find_duplicate(nums):
    merge_sort(nums, 0, len(nums))

    verifier = []
    for numero in nums:
        if (isinstance(numero, int)):
            if numero in verifier:
                return numero
            else:
                verifier.append(numero)
        else:
            return False

    if (len(verifier) == len(nums)) or not nums:
        return False


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    l_i, r_i = 0, 0

    for general_index in range(start, end):
        if l_i >= len(left):
            numbers[general_index] = right[r_i]
            r_i = r_i + 1
        elif r_i >= len(right):
            numbers[general_index] = left[l_i]
            l_i = l_i + 1
        elif left[l_i] < right[r_i]:
            numbers[general_index] = left[l_i]
            l_i = l_i + 1
        else:
            numbers[general_index] = right[r_i]
            r_i = r_i + 1

# if __name__ == "__main__":
#     permanence_period = [2, -1, -1]
#     x = find_duplicate(permanence_period)
#     print(x)