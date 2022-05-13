import math
class Rational:
    def __init__(self, _n, _d=1):
        nod = math.gcd(_n, _d)
        _n, _d = _n / nod, _d / nod
        if _d < 0:
            _n = _n * (-1)
            _d = _d * (-1)
        self._n = int(_n)
        self._d = int(_d)

    def numerator(self):
        return self._n

    def denominator(self):
        return self._d

    def str(self):
        if self._n == 0:
            return f'0'
        elif self._d == 1:
            return f'{self._n}'
        elif self._d == 0:
            return f'ERROR!'
        else:
            return f'{self._n}/{self._d}'

    def as_number(self):
        if self._n == 0:
            return 0
        elif self._d == 1:
            return self._n
        elif self._d == 0:
            return f'ERROR!'
        else:
            return self._n/self._d

    def __add__(self, frac):
        new_n = self._n * frac._d + self._d * frac._n
        new_d = self._d * frac._d
        return (new_n / math.gcd(new_d, new_n))/(new_d / math.gcd(new_d, new_n))

    def add_in_place(self, frac):
        self._n = self._n * frac._d + self._d * frac._n
        self._d = self._d * frac._d
        # return (self._n / math.gcd(self._n, self._d))/(self._d / math.gcd(self._n, self._d))

    def __sub__(self, frac):
        new_n = self._n * frac._d - self._d * frac._n
        new_d = self._d * frac._d
        return (new_n / math.gcd(new_d, new_n))/(new_d / math.gcd(new_d, new_n))

    def sub_in_place(self, frac):
        self._n = self._n * frac._d - self._d * frac._n
        self._d = self._d * frac._d
        # return f'{int(self._n / math.gcd(self._n, self._d))}/{int(self._d / math.gcd(self._n, self._d))}'

    def __mul__(self, frac):
        new_n = self._n * frac._n
        new_d = self._d * frac._d
        return (new_n / math.gcd(new_d, new_n))/(new_d / math.gcd(new_d, new_n))

    def mul_in_place(self, frac):
        self._n = self._n * frac._n
        self._d = self._d * frac._d
        # return f'{int(self._n / math.gcd(self._d, self._n))}/{int(self._d / math.gcd(self._d, self._n))}'

    def __truediv__(self, frac):
        new_n = self._n * frac._d
        new_d = self._d * frac._n
        return (new_n / math.gcd(new_d, new_n))/(new_d / math.gcd(new_d, new_n))

    def div_in_place(self, frac):
        self._n = self._n * frac._n
        self._d = self._d * frac._d
        # return f'{int(self._n / math.gcd(self._n, self._d))}/{int(self._d / math.gcd(self._n, self._d))}'

    def __iadd__(self, frac):
        self._n = self._n * frac._d + self._d * frac._n
        self._d = self._d * frac._d
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self

    def __isub__(self, frac):
        self._n = self._n * frac._d - self._d * frac._n
        self._d = self._d * frac._d
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self

    def __imul__(self, frac):
        self._n = self._n * frac._n
        self._d = self._d * frac._d
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self

    def __idiv__(self, frac):
        self._n = self._n * frac._d
        self._d = self._d * frac._n
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self

    def __eq__(self, frac):
        if self._n == frac._n and self._d == frac._d:
            return True
        else:
            return False

    def __ne__(self, frac):
        if self.__eq__(frac):
            return False
        else:
            return True

    def __lt__(self, frac):
        if self._n / self._d > frac._n / frac._n:
            return True
        else:
            return False

    def __le__(self, frac):
        if self._n / self._d >= frac._n / frac._n:
            return True
        else:
            return False

    def __gt__(self, frac):
        if self.__lt__(frac):
            return False
        else:
            return True

    def __ge__(self, frac):
        if self.__le__(frac):
            return False
        else:
            return True

    def __radd__(self, num):
        self._n = num * self._d + self._n
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self

    def __rsub__(self, num):
        self._n = num * self._d - self._n
        self._n = int(self._n / math.gcd(self._n, self._d))
        self._d = int(self._d / math.gcd(self._n, self._d))
        return self


def series(n):
    return sum([1 / i for i in range(1, n + 1)])


def irreducible(n):
    return [f'{i}/{n}' for i in range(n + 1) if math.gcd(i, n) == 1 and i != 1]



a = Rational(2, -3)
b = Rational(5, 4)
print(a.str())
print(b.str())
c = a.__add__(b)
print(a.str(), b.str(), c)
a.add_in_place(b)
print(a.str(), b.str())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.__iadd__(b))
print(a.__isub__(b))
print(a.__eq__(b))
print(a.__gt__(b))
print(b.__lt__(a))
print(a.__le__(b))
print(2 + a)
print(series(5))
print(irreducible(4))
