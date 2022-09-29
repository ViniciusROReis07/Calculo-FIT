from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(x**2 - 10*x + 21,  markers=[
    {'args': [3, 0, 'go'], 'color':'blue'},
    {'args': [7, 0, 'go'], 'color':'blue'},
    {'args': [0, 21, 'go'], 'color':'blue'},
    {'args': [5, -4, 'go'], 'color':'blue'},
    {'args': [-1, 32, 'go'], 'color':'orange'},
    {'args': [9, 12, 'go'], 'color':'orange'},
    {'args': [2, 5, 'go'], 'color':'orange'},]
    , title="1 - t) y = x2 −10x +21")
