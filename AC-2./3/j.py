from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(1/x,  markers=[
    {'args': [2.5, 0.45, 'go'], 'color':'orange'},
    {'args': [1, 1, 'go'], 'color':'orange'},
    {'args': [-1, -1, 'go'], 'color':'orange'},]
    , title="1 - j) y = 1/x", ylim=[-10, 10], xlim=[-10, 10])
