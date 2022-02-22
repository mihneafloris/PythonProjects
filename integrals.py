from scipy.integrate import quad
def integrand(x):
    return (1+x**2)/(1+x**4)
I = quad(integrand, 0, 1)
print(I)
