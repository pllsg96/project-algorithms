def is_palindrome_iterative(word):

    if (len(word) <= 0):
        return False

    low_index = 0
    high_index = len(word) - 1

    while low_index < high_index:
        if word[low_index] != word[high_index]:
            return False

        low_index += 1
        high_index -= 1

    return True


if __name__ == "__main__":
    xy = is_palindrome_iterative('TENET')
    print(xy)
