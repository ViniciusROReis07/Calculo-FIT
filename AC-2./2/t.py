from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(ln(x**2),  markers=[
    {'args': [1, 0, 'go'], 'color':'blue'},
    {'args': [-1, 0, 'go'], 'color':'blue'},
    {'args': [2.5, 1.8, 'go'], 'color':'orange'},
    {'args': [-2.5, 1.8, 'go'], 'color':'orange'},
    {'args': [-7.5, 4, 'go'], 'color':'orange'},]
    , title="1 - t) y = ln (x2)", ylim=[-10, 10], xlim=[-10, 10])
