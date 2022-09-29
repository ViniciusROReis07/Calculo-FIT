from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(x**2 - 25,  markers=[
    {'args': [-5, 0, 'go'], 'color':'blue'},
    {'args': [5, 0, 'go'], 'color':'blue'},
    {'args': [0, -25, 'go'], 'color':'blue'},
    {'args': [6, 11, 'go'], 'color':'orange'},
    {'args': [-6, 11, 'go'], 'color':'orange'},
    {'args': [7, 24, 'go'], 'color':'orange'},]
    , title="1 - r) y = x2 − 25")
