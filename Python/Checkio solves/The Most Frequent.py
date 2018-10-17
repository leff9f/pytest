def most_frequent(data: list) -> str:
    """
        determines the most frequently occurring string in the sequence.
    """
    # your code here
    return max(data, key=data.count)

if __name__ == '__main__':

    most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ])

    most_frequent(['a', 'a', 'bi', 'bi', 'bi'])
