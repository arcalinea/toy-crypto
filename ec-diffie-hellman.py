# Toy elliptic curve diffie hellman key exchange

from curve import EllipticCurve, Point

class Person(object):
    def __init__(self, secret_key):
        self.curve = EllipticCurve(65, -65, 3077783)
        self.generatorPoint = Point(1, 1, self.curve)

        self.secret_key = secret_key
        self.received = None

    def send(self):
        print str(self.generatorPoint)
        return self.secret_key * self.generatorPoint

    def receive(self, num):
        self.received = num
        print num

    def compute_shared_secret(self):
        return self.secret_key * self.received

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
