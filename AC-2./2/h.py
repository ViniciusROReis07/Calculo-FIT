from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(sec(x) ,markers=[
    {'args': [0, 1, 'go'], 'color':'blue'},
    {'args': [-3.13, -1, 'go'], 'color':'orange'},
    {'args': [6.25, 1, 'go'], 'color':'orange'},
    {'args': [-6.40, 1, 'go'], 'color':'orange'},
    ], title="2 - h) y = sec (x)", ylim=[-5, 5], xlim=[-10, 10])
