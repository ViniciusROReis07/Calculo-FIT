from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(x**2 + 10*x - 21,  markers=[
    {'args': [-11.7, 0, 'go'], 'color':'blue'},
    {'args': [1.7, 0, 'go'], 'color':'blue'},
    {'args': [0, -21, 'go'], 'color':'blue'},
    {'args': [-5, -46, 'go'], 'color':'blue'},
    {'args': [4.7, 50, 'go'], 'color':'orange'},
    {'args': [-7.6, -40, 'go'], 'color':'orange'},
    {'args': [-1, -31, 'go'], 'color':'orange'},]
    , title="1 - v) y = x2 +10x −21")
