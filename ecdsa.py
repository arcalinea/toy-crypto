# Toy elliptic curve digital signature algorithm

import hashlib
import random

from curve import Curve, Point

# privkey: a random integer less than the  order  of  the  curve
# pubkey: point on curve, privkey * generatorPoint

# To sign: take hash of msg
# Take leftmost bits of hash, bit length of group order n
# Select random int from [1, n-1]
# calculate curve pt of random int * generator pt
# calculate modular inverse of x coordinate: r = x1 % n
# Calculate s = k^-1 (leftmost bits + r * privkey) % n
# sig is pair (r, s)

msg = "Hello world!"
e = hashlib.sha256(msg).hexdigest()
print e
z = e[0]
print z

curve = Curve(65, -65, 3077783)
# curve = Curve(65, -65, 103)
generatorPoint = Point(1, 1, curve)
n = generatorPoint.get_order()
print 'order n', n

# Select random k = random int from [1, n-1]
# n = integer order of G, means that n x G = 0. TODO: What is n?
# Must be different for each msg, otherwise key can be extracted.
# Must be sufficiently random
# To ensure that k is unique, once may generate deterministic signatures by deriving k from the message and private key
# What is n?
k = random.choice(range(1, curve.prime - 1))
print 'k', k

privkey = random.choice(range(1, curve.prime - 1))
print 'privkey', privkey

print curve.prime
for k in range(1, 220000):
    if curve.has_point(k):
        print k

# calculate curve pt of random int * generator pt
point = generatorPoint * k
print point

# calculate modular inverse of x coordinate: r = x1 % n
r = point.x % curve.prime
print r

# Calculate s = k^-1 (leftmost bits + r * privkey) % n
# s = k ** -1 (z + r * privkey) % curve.prime
# print s
# (z + (r * privkey))
