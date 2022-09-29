from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(-15  -3*x,  markers=[
    {'args': [-5, 0, 'go'], 'color':'blue'},
    {'args': [0, -15, 'go'], 'color':'blue'},
    {'args': [-10, 15, 'go'], 'color':'orange'},
    {'args': [5, -30, 'go'], 'color':'orange'},
    {'args': [10, -45, 'go'], 'color':'orange'},]
    , title="1 - l) y = −15 −3x")
