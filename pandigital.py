# Pandigital Module

"""From https://projecteuler.net/
'We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.'

I'll make up the term 'partially pandigital' to mean a number which, when catted
with some other chars, *could* form a pandigital number. In other words, a
string with length less than ten, containing only number characters, each of
which appears only once."""

def isPartiallyPandigital(number):
    """Given an integer, return True if the integer is partially pandigital.

    A partially pandigital number is a number which, when catted with some other
    chars, *could* form a pandigital number. For example 9582 is partially
    pandigital since, when catted with 13467, it forms a pandigital number. 33,
    however, is not, since it repeats a digit.

    This function is slow. (RP, 2014-09-21)"""

    numString = sorted(str(number))
    if numString[0] == 0:
        return False
    for i in range(len(numString)-1):
        if numString[i]==numString[i+1]:
            return False
    return True

def isPandigital(number):
    """Given an integer, return True if the integer is pandigital.

    We shall say that an n-digit number is pandigital if it makes use of all the
    digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
    through 5 pandigital.

    This function is slow. (RP, 2014-09-21)"""

    numString = str(number)
    if len(numString) != 9:
        return False
    numString = sorted(numString)
    # print(number,'sss')
    if number[0] == 0:
        return False
    # print(numString)
    for i in range(len(numString)):
        if numString[i] != str(i+1):
            return False
    return True