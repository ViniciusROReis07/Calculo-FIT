from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(x**2 - 4*x,  markers=[
    {'args': [0, 0, 'go'], 'color':'blue'},
    {'args': [4, 0, 'go'], 'color':'blue'},
    {'args': [2, -4, 'go'], 'color':'red'},
    {'args': [-4.6, 40, 'go'], 'color':'orange'},
    {'args': [6, 12, 'go'], 'color':'orange'},
    {'args': [-2, 12, 'go'], 'color':'orange'},]
    , title="1 - p) y = x2 − 4x")
