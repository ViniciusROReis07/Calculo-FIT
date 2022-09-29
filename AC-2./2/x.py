from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot((3-x)/(x-5) ,markers=[
    {'args': [0,-0.6, 'go'], 'color':'blue'},
    {'args': [3, 0, 'go'], 'color':'blue'},

    {'args': [7, -2, 'go'], 'color':'orange'},
    {'args': [4, 1, 'go'], 'color':'orange'},
    {'args': [6, -3, 'go'], 'color':'orange'},
    ], title="2 - x) y =3−x/x−5", ylim=[-20, 20], xlim=[-10, 10])