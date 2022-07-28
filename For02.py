def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    s = ''
    for i in range(n):
        if i == n-1:
            s += str(i)
        else:
            s += str(i) + ','
    return s