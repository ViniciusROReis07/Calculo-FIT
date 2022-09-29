from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot( x**4-3*x**3-2*x,markers=[
    {'args': [0, 0, 'go'], 'color':'blue'},
    {'args': [3.19, 0, 'go'], 'color':'blue'},
    {'args': [2.3, -13.13, 'go'], 'color':'blue'},
    {'args': [3.5, 20, 'go'], 'color':'orange'},
    {'args': [-1.5, 20, 'go'], 'color':'orange'},
    {'args': [3.40, 10, 'go'], 'color':'orange'},
    {'args': [3.40, 10, 'go'], 'color':'orange'},
    ], title="2 - c) y = x4 − 3x 3 + 2x", ylim=[-30, 30], xlim=[-15, 15])
