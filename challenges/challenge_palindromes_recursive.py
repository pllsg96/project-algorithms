def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    print(low_index, high_index)

    if (len(word) == 0):
        return False

    elif (low_index >= high_index):
        return True

    elif (word[low_index] != word[high_index]):
        return False

    elif is_palindrome_recursive(word, low_index + 1, high_index - 1):
        return True

    return False


if __name__ == "__main__":
    x = is_palindrome_recursive('TENET', 0, 4)
    print(x)
