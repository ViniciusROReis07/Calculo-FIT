from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(-e**x,  markers=[
    {'args': [0, -1, 'go'], 'color':'blue'},
    {'args': [0.45, -1.48, 'go'], 'color':'orange'},
    {'args': [1, -2.71, 'go'], 'color':'orange'},
    {'args': [2, -7.5, 'go'], 'color':'orange'},]
    , title="1 -p) y = −ex", ylim=[-10, 10], xlim=[-5, 5])
