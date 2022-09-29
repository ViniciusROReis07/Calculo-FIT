from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")

plot(x**2 + 25,  markers=[
    {'args': [0, 25, 'go'], 'color':'blue'},
    {'args': [-5, 50, 'go'], 'color':'orange'},
    {'args': [5, 50, 'go'], 'color':'orange'},
    {'args': [-10, 125, 'go'], 'color':'orange'},]
    , title="1 - s) y = x2 +25")
