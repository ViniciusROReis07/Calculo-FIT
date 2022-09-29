from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(log(x),  markers=[
    {'args': [1, 0, 'go'], 'color':'blue'},
    {'args': [9, 2.20, 'go'], 'color':'orange'},
    {'args': [4, 1.43, 'go'], 'color':'orange'},
    {'args': [2, 0.7, 'go'], 'color':'orange'},]
    , title="1 -q) y = log(x)", ylim=[-10, 10], xlim=[-10, 10])
