from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(csc(x) ,markers=[
    {'args': [7.7, 1, 'go'], 'color':'orange'},
    {'args': [3.9, -1.5, 'go'], 'color':'orange'},
    {'args': [-3.7, 2, 'go'], 'color':'orange'},
    ], title="2 - i) y = cossec(x)", ylim=[-5, 5], xlim=[-10, 10])
