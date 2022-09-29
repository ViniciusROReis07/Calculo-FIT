from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(3-ln(x),  markers=[
    {'args': [5, 1.43, 'go'], 'color':'orange'},
    {'args': [7.5, 1, 'go'], 'color':'orange'},
    {'args': [1.80, 2.5, 'go'], 'color':'orange'},]
    , title="1 - v) y = 3− ln(x)", ylim=[-10, 10], xlim=[-10, 10])
