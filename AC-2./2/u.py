from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})
from math import e

x = Symbol("x")

plot((ln(x))**2,  markers=[
    {'args': [1, 0, 'go'], 'color':'blue'},
    {'args': [7.5, 4.1, 'go'], 'color':'orange'},
    {'args': [2, 0.5, 'go'], 'color':'orange'},
    {'args': [5, 2.6, 'go'], 'color':'orange'},]
    , title="1 - u) y = (ln(x))2", ylim=[-10, 10], xlim=[-10, 10])
