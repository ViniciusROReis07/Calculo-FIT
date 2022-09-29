from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot(e**x,  markers=[
    {'args': [0, 1, 'go'], 'color':'blue'},
    {'args': [0.95, 2.5, 'go'], 'color':'orange'},
    {'args': [1.4, 4, 'go'], 'color':'orange'},
    {'args': [2, 7.5, 'go'], 'color':'orange'},]
    , title="1 - k) y = e", ylim=[-10, 10], xlim=[-15, 15])
