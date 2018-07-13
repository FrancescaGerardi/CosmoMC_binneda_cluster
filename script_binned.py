import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(here,'./python')))
import planckStyle as s
from pylab import *


from getdist import plots, MCSamples
import getdist

print('Version: ',getdist.__version__)

import GetDistPlots

import planckStyle

g = planckStyle.getSubplotPlotter(chain_dir = './chains')
#g = planckStyle.getSinglePlotter(width_inch=5, chain_dir = './chains')


roots = ['Horn_binned_prior+JLA+BAO']
params = [u'binw1', u'binw2', u'binw3', u'binw4', u'H0',u'omegam',u'omegal']
#params = [u'omegam', u'omegal']
#param_3d = 'H0'
g.settings.solid_contour_palefactor = 0.8
g.triangle_plot(roots, params, filled=[True], legend_labels=['Horn\_prior+JLA+BAO\_9.83'], legend_loc='upper right')

#g.triangle_plot(roots, params, plot_3d_with_param=param_3d ,filled=[False], legend_labels=['Horn\_prior+JLA+BAO\_13'], legend_loc='upper right')

g.export('./binned_4.png')


