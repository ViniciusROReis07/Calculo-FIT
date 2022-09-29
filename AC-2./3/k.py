from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")
y = Symbol("y")


plot(x**x/x,  markers=[
    {'args': [0, 12, 'go'], 'color':'blue'},
    {'args': [2.5, 12, 'go'], 'color':'orange'},
    {'args': [-2.5, 12, 'go'], 'color':'orange'},
    {'args': [7.5, 12, 'go'], 'color':'orange'},]
    , title="1 - b) y = 12", ylim=[-20, 20], xlim=[-10, 10])
