#!/bin/bash
#PBS -N apptainer-O76024-donphan
#PBS -l nodes=1:ppn=4
#PBS -l walltime=1:00:00
#PBS -m ae
#PBS -M alexander.botzki@vib.be
#PBS -o $PBS_JOBID.stdout
#PBS -e $PBS_JOBID.stderr

# eventually load other modules
#module purge
#module load Package1 Package2 Package3

# go to the (current) working directory (optional, if this is the
# directory where you submitted the job)
cd /tmp
mkdir /tmp/$USER

echo Start Job
date

APPTAINER_CACHEDIR=/tmp/ \
APPTAINER_TMPDIR=/tmp/ \
apptainer build --fakeroot /tmp/$USER/tensorflow-23.06-tf2-py3.sif \
docker://nvcr.io/nvidia/tensorflow:23.06-tf2-py3

mv  /tmp/$USER/tensorflow-23.06-tf2-py3.sif $VSC_DATA/apptainer-course/

date
echo End Job
