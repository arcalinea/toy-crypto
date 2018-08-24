
def exp(*args):
    exp = 0
    for i, var in enumerate(args):
        if i == 0: 
            exp = var
        else: 
            exp *= var
    return 2**exp

# Definition for Weil Pairings
# e(P, Q + R) = e(P, Q) * e(P, R)
# e(P + S, Q) = e(P, Q) * e(S, Q)

# Example of pairings using real numbers:
# e(3, 4+ 5) = 2^(3 * 9) = 2^27

P = 3
Q = 4
R = 5
S = 6

print "Definition for Weil Pairings:"
print "exp(P, Q + R) = exp(P, Q) * exp(P, R)"
print exp(P, Q + R), "==", exp(P, Q) * exp(P, R)
print exp(P, Q + R) == exp(P, Q) * exp(P, R)
print "Example of pairings using real numbers:"
print "exp(3, 4+ 5) = 2**(3 * 9) = 2**27"
print exp(3, 4+ 5), "==", 2**(3 * 9), "==", 2**27
print exp(3, 4 + 5) == 2**(3 * 9) == 2**27

print exp(P + S, Q) == exp(P, Q) * exp(S, Q)

