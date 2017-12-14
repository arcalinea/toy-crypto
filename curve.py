# Toy elliptic curve
# Used https://github.com/markusju/elliptic-curves as reference

class EllipticCurve(object):
    # y^2 = x^3 + a*x + b
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        # prime modulus which constitutes the finite field in which the curve lies
        self.prime = p

    def __str__(self):
        return 'y^2 = x^3 + %sx + %s' % (self.a, self.b)

    def __repr__(self):
      return str(self)

    def get_points(self):
        list = []
        for x in range(0, self.prime):
            y2 = (x**3 + self.a*x + self.b) % self.prime
            y = y2 / 2
            if not y.is_integer() or y2 == 0:
                continue
            y = int(y)
            list.append(Point(x, y % self.prime, self))
            if not list[-1].is_infinity():
                list.append(Point(x, -y % self.prime, self))
        return list

class Point:
    def __init__(self, x, y, curve):
        # Didn't we already mod y by prime above?
        self.x = x % curve.prime
        self.y = y % curve.prime
        self.curve = curve

        @staticmethod
        def invert(x, p):
            # Fermat's
            return pow(x, p-2, p)

        def is_infinity(self):
            return self.x <=0 and self.y <= 0

        def __str__(self):
            print "Calling str"
            return "{0}, {1}".format(str(self.x), str(self.y))

        def __repr__(self):
            return str(self)

        def __mul__(self, other):
            print "Calling mul"
            if not isinstance(other, int):
                raise TypeError("unsup")
            spoint = Point(0, 0, self.curve)
            for i in range(1, other+1):
                spoint += self
            return spoint
