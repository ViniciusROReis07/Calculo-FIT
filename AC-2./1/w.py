from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(-x**2 - 10*x + 21,  markers=[
    {'args': [-11.7, 0, 'go'], 'color':'blue'},
    {'args': [1.7, 0, 'go'], 'color':'blue'},
    {'args': [0, 21, 'go'], 'color':'blue'},
    {'args': [-5, 46, 'go'], 'color':'blue'},
    {'args': [0.80, 12.5, 'go'], 'color':'orange'},
    {'args': [-8, 37, 'go'], 'color':'orange'},
    {'args': [-1.8, 36, 'go'], 'color':'orange'},]
    , title="1 - w) y = −x2 −10x +21")
