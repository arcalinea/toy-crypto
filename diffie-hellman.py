# Toy diffie-hellman key exchange

# Use multiplicative group of integers modulo a prime, p
P = 23
# Base g is a primitive group modulo p
G = 5

class Person(object):
    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.received = None

    def send(self):
        return G ** self.secret_key % P

    def receive(self, num):
        self.received = num
        print num

    def compute_shared_secret(self):
        return self.received ** self.secret_key % P

# Try picking different secrets to derive different shared secrets
alice = Person(secret_key=7)
print "Alice picks private secret:", alice.secret_key
bob = Person(secret_key=3)
print "Bob picks private secret:", bob.secret_key

print "\nMultiply the group G by itself priv_secret number of times, modulo P, and send that."
print "Alice sends Bob:"
bob.receive(
    alice.send()
)

print "Bob sends Alice:"
alice.receive(
    bob.send()
)

print "\n~*~*~*~ Math Magic ~*~*~*~"
print "Multiply the number received by itself priv_secret number of times, modulo P:"
print "Alice computes shared secret:", alice.compute_shared_secret()
print "Bob computes shared secret:", bob.compute_shared_secret()
