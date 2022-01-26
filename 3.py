# from sympy.plotting import plot
# from sympy.abc import x,pi
# from sympy.functions import sin,cos
# plot((2*sin(x),(x,-6,6)),(cos(x+pi/4),(x,-5,5)))

# from pylab import rc
# from sympy import plot_implicit as pt,Eq
# from sympy.abc import x,y
# rc('font',size=16);rc("text",usetex=True)
# pt(Eq((x-1)**2+(y-2)**3,4),(x,-6,6),(y,-2,4),xlabel='$x$',ylabel='$y$')

from sympy import *
x=symbols('x')
print(limit(sin(x)/x,x,0))
print(limit(pow(1+1/x,x),x,oo))



