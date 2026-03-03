import sympy as sm
import numpy as np

sm.init_printing(use_latex="mathjax")

theta = sm.Function("theta")
t = sm.symbols("t")

theta_0 = sm.symbols("theta_0")
theta_derived_0 = sm.symbols("theta_derived_0")
lhs = sm.Eq(theta(t).diff(t, 2) + 0.4 * theta(t).diff(t) + 100 * theta(t),0)
result = sm.dsolve(
    lhs,
    ics={theta(t).subs(t, 1): theta_0,
         (theta(t).diff(t)).subs(t, 0): theta_derived_0},
)
print(result)
