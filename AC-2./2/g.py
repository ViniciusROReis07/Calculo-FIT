from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(cot(x) ,markers=[
    {'args': [-7.9, 0, 'go'], 'color':'blue'},
    {'args': [-4.7, 0, 'go'], 'color':'blue'},
    {'args': [-1.5, 0, 'go'], 'color':'blue'},
    {'args': [1.5, 0, 'go'], 'color':'blue'},
    {'args': [4.7, 0, 'go'], 'color':'blue'},
    {'args': [7.8, 0, 'go'], 'color':'blue'},
    {'args': [7.10, 1, 'go'], 'color':'orange'},
    {'args': [2.5, -1.5, 'go'], 'color':'orange'},
    {'args': [-4, -0.98, 'go'], 'color':'orange'},
    ], title="2 - g) y = cotg(x)", ylim=[-5, 5], xlim=[-10, 10])
