class Polynomial:

    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        return sum(self.coefficients[i] * x ** i for i in range(len(self.coefficients)))

    def __add__(self, polym):
        coef1 = self.coefficients
        coef2 = polym.coefficients
        if len(coef1) < len(coef2):
            coef1 += [0] * (len(coef2) - len(coef1))
        else:
            coef2 += [0] * (len(coef1) - len(coef2))
        return Polynomial([coef1[i] + coef2[i] for i in range(len(coef1))])


poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))