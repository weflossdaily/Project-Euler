
# Project Euler #120

# rems(a, pwr) returns a subset of the possible remainders
#
#     AllOfThem(a) := { 2 } union { r(a, n) for all natural n }  (1)
#     with
#     r(a, n) := (a+1)**n + (a-1)**n mod a**2                    (2)
#     where a > 2 .
#
# That is, rems(a, pwr) is a subset of AllOfThem(a).
# It uses the fact that AllOfThem(a) is equivalent to
#
#     { 2 } union { 2*(2*j + 1) * a mod a**2 for natural j }     (3).
#
# Their equivalence follows from analysis of r(a, n) .
# 
# The argument 'pwr' is related to the upper end of the range
# searched when calculating the set (it's the end of the loop). 
# I guessed, after playing with some numbers, that pwr = a
# is sufficiently large to find all member of AllOfThem(a).
#
# That is, it's probably the case that for all p >= a
# 
#     rems(a, p) = AllOfThem(a)                                  (4).
#
# In particular, p = a suffices. 
# That's good, because AllOfThem(a) is what we're after.
# 
def rems(a, pwr):
    lastJ = ((a - 2) // 4 + 1) * pwr
    def coeff(j):
        return 4*j + 2

    result = set([2]) | \
        set(coeff(j) * a % a**2 for j in range(1, lastJ + 1))

    return result

# This uses assumption (4), as stated above.
#
def maxMod(a):
    return max(rems(a, a))

# Project Euler #120 asks for the sum of the maximal remainders
# for a in [3, 1000].
#
print(sum(maxMod(a) for a in range(3, 1000 + 1)))
