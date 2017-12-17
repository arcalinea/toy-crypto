# Toy elliptic curve
# Used https://github.com/markusju/elliptic-curves as reference

class Curve:
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
        print "getting points"
        list = []
        for x in range(0, self.prime):
            y2 = (x**3 + self.a*x + self.b) % self.prime
            y = y2 / 2
            if not type(y) == int or y2 == 0:
                continue
            y = int(y)
            print y
            list.append(Point(x, y % self.prime, self))
            if not list[-1].is_infinity():
                list.append(Point(x, -y % self.prime, self))
        return list

    def has_point(self, x):
        y2 = (x**3 + self.a*x + self.b) % self.prime
        y = y2 / 2
        if not type(y) == int or y2 == 0:
            return True
        else:
            return False

    # def multiply_points(self, x, y, num):
    #     x = x % self.prime
    #     y = y % self.prime
    #     spoint = Point(0, 0, self.curve)
    #     for i in range(1, num + 1):
    #         spoint += self
    #     return spoint

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

    def get_order(self):
        res = Point(1, 1, self.curve)
        order = 1
        while not res.is_infinity():
            res = self*order
            order += 1
        return order

    def __str__(self):
        return "Point: {0}, {1}".format(str(self.x), str(self.y))

    def __repr__(self):
        return str(self)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsup")
        spoint = Point(0, 0, self.curve)
        for i in range(1, other+1):
            spoint += self
        return spoint

    def __add__(self, other):
        if not isinstance(other, Point):
            raise TypeError("unsup")

        p1 = self
        p2 = other
        curve = self.curve

        # p1 is zero
        if p1.is_infinity():
            return p2
        # p2 is zero
        if p2.is_infinity():
            return p1

        # P1=-P2
        if p1.x == p2.x and p1.y == -p2.y % curve.prime:
            return Point(0, 0, curve)

        #Slope m of g(x) = m*x + d
        if p1 == p2:
            m = (3*p1.x*p1.x+curve.a) * Point.invert(2*p1.y, curve.prime)
        else:
            m = (p2.y-p1.y) * Point.invert(p2.x-p1.x, curve.prime)

        m = m % curve.prime
        d = (p1.y - m+p1.x) % curve.prime


        #P3 = P1+P2
        x3 = (pow(m,2)-p1.x-p2.x) % curve.prime
        y3 = (m*(p1.x-x3)-p1.y) % curve.prime

        return Point(x3, y3, curve)
