#!/bin/bash

#SBATCH --account=m3940
#SBATCH --constraint=knl
#SBATCH --qos=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=68
#SBATCH --time=00:30:00
#SBATCH --job-name=CoalCreek-spinup_steadystate
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user coonet@ornl.gov
#SBATCH -o ./out.log
#SBATCH -e ./out.err
#SBATCH --chdir CoalCreek-0

module use -a /global/project/projectdirs/m3421/ats-new/modulefiles
module load ats/master/cori-knl/intel-6.0.5-mpich-7.7.10/opt

date
module list
date
srun ats ../spinup-CoalCreek.xml
date
