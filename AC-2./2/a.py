from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(x**3 - 5*x**2 +6*x + 8 ,markers=[
    {'args': [0,8, 'go'], 'color':'blue'},
    {'args': [0.78, 10.11, 'go'], 'color':'blue'},
    {'args': [-0.76, 0, 'go'], 'color':'blue'},
    {'args': [2.5, 7.36, 'go'], 'color':'blue'},

    {'args': [3.9, 15, 'go'], 'color':'orange'},
    {'args': [-1.21, -7.5, 'go'], 'color':'orange'},
    {'args': [1.7, 8.6, 'go'], 'color':'orange'},
    ], title="2 - a) y = x3 − 5x 2 + 6x + 8", ylim=[-20, 20], xlim=[-10, 10])