from scipy import optimize
def f(x):
    return x**3 -5*x**2+11*x-6

root=optimize.newton(f,0.8)

print(root)
