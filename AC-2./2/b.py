

from sympy import *
from sympy.plotting import *
import seaborn as sns
sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

x = Symbol("x")

plot(-x**3 - 5*x**2 -6*x - 8 ,markers=[
    {'args': [-4, 0, 'go'], 'color':'blue'},
    {'args': [0, -8, 'go'], 'color':'blue'},
    {'args': [-2.5, -8.6, 'go'], 'color':'blue'},
    {'args': [-0.7, -5.88, 'go'], 'color':'blue'},
    
    {'args': [-4.73, 15.3, 'go'], 'color':'orange'},
    {'args': [0.63, -14, 'go'], 'color':'orange'},
    {'args': [-4.55, 10, 'go'], 'color':'orange'},
    ], title="2 - b) y = −x3 +5x 2 − 6x − 8", ylim=[-20, 20], xlim=[-10, 10])