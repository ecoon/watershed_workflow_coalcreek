import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import colors

dirnames = dict()
dirnames['CoalCreek'] = '.'
#dirnames['rock vG curve'] = 'cades2/transient-rock2'
#dirnames['subsurface BC'] = 'cades2/transient-bc2'
#dirnames['double PT alpha'] = 'cades2/transient-transpiration2'
#dirnames['nersc'] = 'nersc'

#obsname = '/Users/uec/research/water/problems/CoalCreek-production/exasheds-campaign1/data_preprocessed/CoalCreek_outlet_daily_discharge2.csv'
obsname = None

surface_area = 48577909.581937484 # m^2

if len(dirnames) == 2:
    cm = colors.enumerated_colors(4)
    cm = [cm[0], cm[3]]
    #cm = [cm[3], cm[2]]
elif len(dirnames) == 3:
    cm = colors.enumerated_colors(4)
    cm = [cm[0],cm[3],cm[2]]
else:
    cm = colors.enumerated_colors(len(dirnames))

fig = plt.figure()
axs = fig.subplots(3,1)
axs = list(axs)
axs.append(axs[1].twinx())

df = dict()
for key,dir in dirnames.items():
    df[key] = pd.read_csv(f'{dir}/water_balance.dat', comment='#')

if obsname is not None:
    obs = pd.read_csv(obsname)

runoff_keys = ['runoff generation [mol d^-1]', 'watershed boundary discharge [mol d^-1]']

for i,key in enumerate(df):
    runoff_key = next(k for k in runoff_keys if k in df[key])
    axs[0].plot(df[key]['time [d]']/365, df[key][runoff_key][:]/55000, label=key, color=cm[i])

    # if i == 0:
    #     axs[0].plot(df[key]['time [d]']/365, df[key]['rain precipitation [m d^-1]'][:]*surface_area, label='rain', color='b')
    #     axs[0].plot(df[key]['time [d]']/365, df[key]['snow precipitation [m d^-1]'][:]*surface_area, label='snow', color='c')

if obsname is not None:
    axs[0].plot(obs['time [d]']/365, obs['discharge [m^3/d]'][:], label='observation', color='k')
axs[0].set_xlabel('time [y]')
axs[0].set_ylabel('runoff [m^3 d^-1]')
axs[0].legend()


et_keys = ['evapotranspiration [m d^-1]', 'total evapotranspiration [m d^-1]']
for i,key in enumerate(df):
    if i == 0:
        axs[3].plot(df[key]['time [d]']/365, df[key]['rain precipitation [m d^-1]'][:], label='rain', color='b')
        axs[3].plot(df[key]['time [d]']/365, df[key]['snow precipitation [m d^-1]'][:], label='snow', color='c')

    et_key = next(k for k in et_keys if k in df[key])
    axs[1].plot(df[key]['time [d]']/365, df[key][et_key][:], label=f'{key} total ET', color=cm[i])
    # axs[1].plot(df[key]['time [d]']/365, df[key]['transpiration [m d^-1]'][:], '--', label=f'{key} T', color=cm[i])
    # axs[1].plot(df[key]['time [d]']/365, df[key]['canopy evaporation [m d^-1]'][:], '-.', label=f'{key} can E', color=cm[i])
    # axs[1].plot(df[key]['time [d]']/365, df[key]['surface evaporation [m d^-1]'][:], '-.', label=f'{key} can E', color=cm[i])

axs[1].set_xlabel('time [d]')
axs[1].set_ylabel('total ET [m d^-1]')
axs[3].set_ylabel('precipitation [m d^-1]')

for i,key in enumerate(df):
    try:
        df[key]['total water content [mol]'] = df[key]['subsurface water content [mol]'].array \
            + df[key]['surface water content [mol]'].array \
            + df[key]['canopy water content [mol]'].array
    except KeyError:
        df[key]['total water content [mol]'] = df[key]['subsurface water content [mol]'].array \
            + df[key]['surface water content [mol]'].array
    #    + df[key]['snow water content [mol]'].array \

for i,key in enumerate(df):
    axs[2].plot(df[key]['time [d]']/365, df[key]['total water content [mol]'][:], label=f'{key}', color=cm[i])

axs[2].set_xlabel('time [y]')
axs[2].set_ylabel('total water [mol]')
plt.show()



