from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(tan(x) ,markers=[
    {'args': [0, 0, 'go'], 'color':'blue'},
    {'args': [-9.4, 0, 'go'], 'color':'blue'},
    {'args': [-6.29,0, 'go'], 'color':'blue'},
    {'args': [-3.13, 0, 'go'], 'color':'blue'},
    {'args': [-3.13, 0, 'go'], 'color':'blue'},
    {'args': [3.15, 0, 'go'], 'color':'blue'},
    {'args': [6.20, 0, 'go'], 'color':'blue'},
    {'args': [9.4, 0, 'go'], 'color':'blue'},
    {'args': [7, 1, 'go'], 'color':'orange'},
    {'args': [2.3, -1, 'go'], 'color':'orange'},
    {'args': [-3.9, -1, 'go'], 'color':'orange'},
    ], title="2 - f) y = tg(x)", ylim=[-5, 5], xlim=[-10, 10])
