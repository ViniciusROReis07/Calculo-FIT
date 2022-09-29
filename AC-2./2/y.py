from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(x**6-4*x**5+3*x**4-2*x**3+5*x-7 ,markers=[
    {'args': [-1.04,0, 'go'], 'color':'blue'},
    {'args': [3.23,0, 'go'], 'color':'blue'},
    {'args': [0, -7, 'go'], 'color':'blue'},
    {'args': [0.8, -3.8, 'go'], 'color':'blue'},
    {'args': [-0.51, -8.9, 'go'], 'color':'blue'},


    {'args': [-1, -3, 'go'], 'color':'orange'},
    {'args': [3.23, -4, 'go'], 'color':'orange'},
    {'args': [3.23, 5, 'go'], 'color':'orange'},
    ], title="2 - y) y = x6 − 4x5 + 3x4 − 2x3 + 5x − 7", ylim=[-15, 15], xlim=[-10, 10])