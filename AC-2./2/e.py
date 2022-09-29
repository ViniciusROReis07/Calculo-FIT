from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(cos(x) ,markers=[
    {'args': [0, 1, 'go'], 'color':'blue'},
    {'args': [-7.9, 0, 'go'], 'color':'blue'},
    {'args': [-4.7, 0, 'go'], 'color':'blue'},
    {'args': [-1.5, 0, 'go'], 'color':'blue'},
    {'args': [1.5, 0, 'go'], 'color':'blue'},
    {'args': [4.7, 0, 'go'], 'color':'blue'},
    {'args': [7.8, 0, 'go'], 'color':'blue'},
    {'args': [6.3, 1, 'go'], 'color':'orange'},
    {'args': [3.15, -1, 'go'], 'color':'orange'},
    {'args': [-3.3, -0.98, 'go'], 'color':'orange'},
    ], title="2 - e) y = cos (x)", ylim=[-5, 5], xlim=[-10, 10])
