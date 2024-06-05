def sum_of_list(numbers):
    """Return the sum of all numbers in a list
    >>> sum_of_list([1, 2, 3])
    6
    >>> sum_of_list([5, 8, 13])
    26
    """
    total = 0
    for number in numbers:
        total += number
    return total

if __name__ == "__main__":
    import doctest
    doctest.testmod()