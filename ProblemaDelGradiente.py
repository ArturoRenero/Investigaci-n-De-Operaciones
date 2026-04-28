import sympy as sp ## << for derivatives
## we can use "x = sp.symbols('x')" as a way to define a symbol 'x'

## > x = sp.symbols('x')
## > f = x**2 + 3*x + 5
## > f_prime = sp.diff(f, x)  # Result: 2*x + 3
##
## Evaluate at a specific point
## > value_at_2 = f_prime.subs(x, 2)  # Result: 7

x1, x2 = 0, 0
t = 0
currentStep = [x1, x2]

## fnObjetivo = ((2*x1*x2) + (2*x2) - (pow(x1, 2)) - (2*pow(x2, 2)))

def FuncionObjetivo(x1Loc, x2Loc):
    #fnObjetivo = ((2*x1*x2)+(2*x2)-(pow(x1, 2))-(2*pow(x2, 2)))
    A = x1Loc
    B = x2Loc
    Step1, Step2, Step3, Step4 = 0, 0, 0, 0
    Step1 = 2*A*B
    Step2 = 2*B
    Step3 = -(pow(A, 2))
    Step4 = -(2*pow(B, 2))
    return (Step1 + Step2 + Step3 + Step4)

x1Deriv = ((2*x2) - (2*x1))
x2Deriv = ((2*x1) + 2 - (4*x2))

nextStep = [x1Deriv, x2Deriv]

x1t = currentStep[0] + (t * nextStep[0])
x2t = currentStep[1] + (t * nextStep[1])

fnObjT = FuncionObjetivo(x1t, x2t)


