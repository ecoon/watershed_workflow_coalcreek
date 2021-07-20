#!/bin/bash

#SBATCH -A ccsi
#SBATCH -p batch
#SBATCH -N 1
#SBATCH -n 32
#SBATCH -c 1
#SBATCH --ntasks-per-node=32
#SBATCH -J CoalCreek-spinup
#SBATCH --mem=64G
#SBATCH -t 1:00:00
#SBATCH -o ./out.log
#SBATCH -e ./out.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=coonet@ornl.gov
#SBATCH --chdir CoalCreek-0

module load ats/master/opt/PE-gnu-4.0
date
mpiexec -n 32 ats --xml_file=../spinup-CoalCreek.xml
date
