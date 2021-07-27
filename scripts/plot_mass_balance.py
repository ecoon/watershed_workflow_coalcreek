import h5py
import pandas
import numpy as np
from matplotlib import pyplot as plt

# surface area
d = h5py.File('ats_vis_surface_data.h5','r')
a_key = list(d['surface-cell_volume.cell.0'].keys())[0]
surf_area = d['surface-cell_volume.cell.0'][a_key][:].sum() # m^2
d.close()

# load data
df = pandas.read_csv('water_balance.dat', comment='#')

# process
time = df['time [d]']
P = df['rain precipitation [m d^-1]']
SM = df['snowmelt [m d^-1]']
ET = df['evapotranspiration [m d^-1]']
Q = df['runoff generation [mol d^-1]']/55500./surf_area
diff = P + SM - ET - Q
water = (df['surface water content [mol]'] + df['subsurface water content [mol]']) / 55500 / surf_area

error = np.cumsum(diff) - (water - water[0])
max_error = error.max()

snow = df['snow water content [mol]'] / 55500 / surf_area
S = df['snow precipitation [m d^-1]']

# plot
fig = plt.figure()

ax = fig.add_subplot(3,1,1)
ax.plot(time, np.cumsum(P), label='P')
ax.plot(time, np.cumsum(SM), label='SM')
ax.plot(time, np.cumsum(ET), label='ET')
ax.plot(time, np.cumsum(Q), label='Q')
ax.plot(time, water - water[0], 'k', label='water')
ax.plot(time, np.cumsum(diff), 'k--', label='P+SM-ET-Q')
ax.plot(time, error, '-.', color='grey', label='error')
ax.legend()

ax.set_title(f'Cumulative sums of fluxes (Inf err: {max_error})')
ax.set_xlabel('time [d]')
ax.set_ylabel('cumulative flux [m]')


ax = fig.add_subplot(3,1,2)
ax.plot(time, P, label='P')
ax.plot(time, SM, label='SM')
ax.plot(time, ET, label='ET')
ax.plot(time, Q, label='Q')
ax.plot(time, error[1:] - error[:-1], '-.', color='grey', label='delta error')
ax.legend()
ax.set_title('fluxes')
ax.set_xlabel('time [d]')
ax.set_ylabel('flux [m / d]')

ax = fig.add_subplot(3,1,3)
ax.plot(time, np.cumsum(S), label='P_snow')
ax.plot(time, np.cumsum(SM), label='SM')
ax.plot(time, snow, 'k', label='snow depth')
ax.plot(time, np.cumsum(S-SM), 'k--', label='Ps - SM')
ax.legend()
ax.set_ylabel('cumulative flux [m]')
ax.set_xlabel('time [d]')
plt.show()
