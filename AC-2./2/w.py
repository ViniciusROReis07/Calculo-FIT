from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot((x**2-12*x+35)/(x-10) ,markers=[
    {'args': [0,-3.5, 'go'], 'color':'blue'},
    {'args': [5, 0, 'go'], 'color':'blue'},
    {'args': [7, 0, 'go'], 'color':'blue'},
    {'args': [6.12, 0.25, 'go'], 'color':'blue'},

    {'args': [8.7, -5, 'go'], 'color':'orange'},
    {'args': [-1.50, -5, 'go'], 'color':'orange'},
    {'args': [9.3, -15, 'go'], 'color':'orange'},
    ], title="2 - w) y =x2−12x+35/x−10", ylim=[-20, 20], xlim=[-10, 10])