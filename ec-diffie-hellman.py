# Toy elliptic curve diffie hellman key exchange

from curve import Curve, Point

class Person(object):
    def __init__(self, secret_key):
        self.curve = Curve(65, -65, 3077783)
        self.generatorPoint = Point(1, 1, self.curve)

        self.secret_key = secret_key
        self.received = None

    def send(self):
        return self.generatorPoint * self.secret_key

    def receive(self, num):
        self.received = num
        print num

    def compute_shared_secret(self):
        return self.received * self.secret_key

alice = Person(secret_key=13)
bob = Person(secret_key=79)

print "Alice sends Bob:"
bob.receive(
    alice.send()
)

print "Bob sends Alice:"
alice.receive(
    bob.send()
)

print "Alice computes shared secret:", alice.compute_shared_secret()
print "Bob computes shared secret:", bob.compute_shared_secret()
