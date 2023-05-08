def is_anagram(first_string, second_string):

    if len(first_string) != len(second_string):
        return (first_string, second_string, False)

    elif not len(first_string) or not len(second_string):
        return (first_string, second_string, False)

    ssa = partition(first_string.lower(), 0, len(first_string) - 1)
    ssb = partition(second_string.lower(), 0, len(second_string) - 1)

    if (ssa[1] == ssb[1]):
        print(ssa[1], ssb[1])
        return ssa[1], ssb[1], True

    elif (ssa[1] != ssb[1]):
        return first_string, second_string, False


def q_sort(word, start, end):
    if start < end:
        p = partition(word, start, end)
        q_sort(word, start, p - 1)
        q_sort(word, p + 1, end)


def partition(word, start, end):
    word_list = list(word)
    pivot = word_list[end]
    delimiter = start - 1

    for i in range(start, end):
        if (word_list[i] <= pivot):
            delimiter = delimiter + 1
            word_list[i], word_list[delimiter] = \
                word_list[delimiter], word_list[i]

    word_list[delimiter + 1], word_list[end] = \
        word_list[end], word_list[delimiter + 1]

    return delimiter + 1, ''.join(word_list)


if __name__ == "__main__":
    x = 'cBa'
    y = 'Cab'
    print(is_anagram(x, y))

    a = 'PEDRA'
    b = 'perda'
    print(is_anagram(a, b))
