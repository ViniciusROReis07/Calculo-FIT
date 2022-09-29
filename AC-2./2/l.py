from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(5**x,  markers=[
    {'args': [0, 1, 'go'], 'color':'blue'},
    {'args': [1, 5, 'go'], 'color':'orange'},
    {'args': [2, 25, 'go'], 'color':'orange'},
    {'args': [3, 125, 'go'], 'color':'orange'},]
    , title="1 - l) y = 5x", ylim=[-150, 150], xlim=[-25, 25])
