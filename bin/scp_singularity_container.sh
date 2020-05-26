#!/bin/bash
export CLUSTER_URI=/data/cephfs/punim1179/aqc-maxcut
export HOST_NAME=mcandrewf@spartan.hpc.unimelb.edu.au

echo 'migrating singularity container to spartan'

scp portable-image.img $HOST_NAME:$CLUSTER_URI
