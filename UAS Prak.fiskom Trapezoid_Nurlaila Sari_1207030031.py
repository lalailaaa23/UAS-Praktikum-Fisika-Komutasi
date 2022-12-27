Trapezoid(a,b):
    def f(x):
        return x**2+x
n = 100
def trapezoid(f,a,b,n=100):
    h=(b-a)/n
    sum = 0.0
    for i in range (1,n):
        x = a+i*h
        sum = sum +f(x)
    integral = (h/2)*(f(a)+2*sum+f(b))
    return integral
integral = trapezoid(f,a,b,n)
print(a,",",round(integral,2))

i in range(0,10):
Trapezoid(i+1,i+2)
