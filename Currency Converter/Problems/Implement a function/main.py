def get_number(num):
    """Return the number one less than the given positive number. 
    If the number is nonpositive, return a string "Enter a positive number!".

    Arguments:
    num -- an integer.
    Return values:
    An integer one less than the input number.
    """
    if num <= 0:
        return 'Enter a positive number!'
    else:
        return num - 1
