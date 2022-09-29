from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(-x**2,  markers=[
    {'args': [0, 0, 'go'], 'color':'blue'},
    {'args': [5, -25, 'go'], 'color':'orange'},
    {'args': [-5, -25, 'go'], 'color':'orange'},
    {'args': [7.5, -56, 'go'], 'color':'orange'},]
    , title="1 - n) y = −x2")
