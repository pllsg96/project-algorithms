def is_anagram(first_string, second_string):

    if not len(first_string) and not len(second_string):
        return (first_string, second_string, False)

    ssa = ''.join(q_sort(first_string.lower()))
    ssb = ''.join(q_sort(second_string.lower()))
    print(ssa, ssb)
    if (ssa == ssb):
        return ssa, ssb, True

    elif (ssa != ssb):
        return ssa, ssb, False


def q_sort(word):
    if len(word) <= 1:
        return word
    pivot = word[0]
    left = []
    right = []
    for letter in word[1:]:
        if letter < pivot:
            left.append(letter)
        else:
            right.append(letter)
    return q_sort(left) + [pivot] + q_sort(right)


if __name__ == "__main__":
    x = 'cBa'
    y = 'Cab'
    print(is_anagram(x, y))

    a = 'ALEgria'
    b = 'alergia'
    print(is_anagram(a, b))
