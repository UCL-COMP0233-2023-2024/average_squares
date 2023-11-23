"""Computation of weighted average of squares."""


def average_of_squares(list_of_numbers, list_of_weights=None):
    """ Return the weighted average of a list of values.
    
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.
    
    Example:
    --------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length

    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """Convert a list of strings into numbers, ignoring whitespace.
    
    Example:
    --------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]

    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


# if __name__ == "__main__":
#     numbers_strings = ["1","2","4"]
#     weight_strings = ["1","1","1"]        
    
#     numbers = convert_numbers(numbers_strings)
#     weights = convert_numbers(weight_strings)
    
#     result = average_of_squares(numbers, weights)
    
#     print(result)



import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate the sum of squares of numbers.")
    parser.add_argument("numbers", nargs="+", type=int, help="List of integers to calculate the squares.")
    parser.add_argument("-weights", nargs="+", type=float, help="List of weights for squares")
    args = parser.parse_args()

    numbers = args.numbers
    weights = args.numbers
    # 使用 numbers 变量进行计算
    sum_of_squares = average_of_squares(numbers, weights)

    # sum_of_squares = sum(x**2 for x in numbers)
    print(f"Sum of squares: {sum_of_squares}")