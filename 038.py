'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9 and
(1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?

Notes:
At first, was going to search integers from 987654321 down. Then I thought it
would be a pain to see which number would be multiplied by (1,2,...,n), that I
would be repeating work. Then I realized the left-most digits are that number,
since they're multiplied by 1. That makes things easier. So, Start with 9,
multiply it by 2, cat to the end of 9, check pandigital, repeat until 9 chars
long. What should we try after 9? 91! Then, 92,93,...98, then 987 etc. How to
quickly enumerate the numbers to try? Map them to integers somehow? how?
Could probably get away with just quickly writing them out.
9,98,97,96,95,94,93,92,91,987,986... Probably not. Use the 9 nested if thing to
check for valid permutations? Make something that, given the current term in the
sequence generates the next? Too much. I'll make up the term 'partially
pandigital' to mean a number which, when catted with some other chars, *could*
form a pandigital number. In other words, a string with length less than ten,
containing only number characters, each of which appears only once. Since the
sequence of factors by which our number will be multiplied must be longer than
just 1, i.e., our number can't just be 987654321, what is an upper bound on our
number? Well, 9876 is the greatest partially pandigital 4-digit number. When
it's multiplied by 2, the result is 5 digits long. Catting them doesn't get you
a pandigital number, but this is an ok upper bound for now. I'll count down from
there, check that the number is partially pandigital, and see if catting the
products gets us a pandigital result. I like this problem because my gut keeps
changing its feeling about where, between 9 and 9876, the number lies.
'''

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
    if len(number) != 9:
        return False
    numString = sorted(number)
    # print(number,'sss')
    if number[0] == 0:
        return False
    # print(numString)
    for i in range(len(numString)):
        if numString[i] != str(i+1):
            return False
    return True

def checkCatProd(number):
    """Given a number as a string, check that its cat-prod is pandigital.

    Concatenated product is described at https://projecteuler.net/problem=38"""
    catProd = ''
    factor = 1
    while len(catProd) < 10:
        # print(catProd)
        catProd += str(int(number) * factor)
        if isPandigital(catProd):
            print(catProd)
            return catProd
        factor += 1
    return ''

for number in range(9876,8,-1):
    # counting down so I can stop when I find one
    if isPartiallyPandigital(number):
        # print(number, " isPartiallyPandigital")
        if checkCatProd(str(number)) != '':
            break