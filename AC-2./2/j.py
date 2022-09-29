from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(2**x,  markers=[
    {'args': [0, 1, 'go'], 'color':'blue'},
    {'args': [1, 2, 'go'], 'color':'orange'},
    {'args': [2, 4, 'go'], 'color':'orange'},
    {'args': [3, 8, 'go'], 'color':'orange'},]
    , title="1 - j) y = 2x", ylim=[-10, 10], xlim=[-20, 20])
