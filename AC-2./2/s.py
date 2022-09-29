from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(ln(x) + 6,  markers=[
    {'args': [1, 6, 'go'], 'color':'orange'},
    {'args': [2.5, 7, 'go'], 'color':'orange'},
    {'args': [5, 7.6, 'go'], 'color':'orange'},]
    , title="1 - s) y = ln(x)+ 6", ylim=[-10, 10], xlim=[-10, 10])
