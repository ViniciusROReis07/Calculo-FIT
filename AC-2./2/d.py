from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(sin(x) ,markers=[
    {'args': [0, 0, 'go'], 'color':'blue'},
    {'args': [-9.4, 0, 'go'], 'color':'blue'},
    {'args': [-6.3, 0, 'go'], 'color':'blue'},
    {'args': [-3.15, 0, 'go'], 'color':'blue'},
    {'args': [3.15, 0, 'go'], 'color':'blue'},
    {'args': [6.25, 0, 'go'], 'color':'blue'},
    {'args': [9.4, 0, 'go'], 'color':'blue'},
    {'args': [2.5, 0.6, 'go'], 'color':'orange'},
    {'args': [4.5, -0.93, 'go'], 'color':'orange'},
    {'args': [-5, 1, 'go'], 'color':'orange'},
    ], title="2 - d) y = sen(x)", ylim=[-5, 5], xlim=[-10, 10])
