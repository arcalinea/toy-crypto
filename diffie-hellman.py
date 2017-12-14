# Toy diffie-hellman key exchange

# Use multiplicative group of integers modulo p
P = 23
# Base g is a primitive group modulo p
G = 5

class Person(object):
    def __init__(self, priv_secret):
        self.priv_secret = priv_secret

    def send(self):
        return G ** self.priv_secret % P

    def receive(self, num):
        self.received = num

    def compute_shared_secret(self):
        return self.received ** self.priv_secret % P


# Try picking different secrets to derive different shared secrets
alice = Person(priv_secret=7)
print "Alice picks private secret:", alice.priv_secret
bob = Person(priv_secret=3)
print "Bob picks private secret:", bob.priv_secret

print "\nMultiply the group G by itself priv_secret number of times, modulo P, and send that:"
a = alice.send()
print "Alice sends Bob:", a
bob.receive(a)

b = bob.send()
print "Bob sends Alice:", b
alice.receive(b)

print "\n~*~*~*~ Math Magic ~*~*~*~"
print "Multiply the number received by itself priv_secret number of times, modulo P:"
a_ss = alice.compute_shared_secret()
print "Alice computes shared secret:", a_ss

b_ss = bob.compute_shared_secret()
print "Bob computes shared secret:", b_ss
