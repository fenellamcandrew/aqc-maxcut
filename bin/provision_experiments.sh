#!/bin/bash
export CLUSTER_URI=/data/cephfs/punim1179/aqc-maxcut
export HOST_NAME=mcandrewf@spartan.hpc.unimelb.edu.au
export RELATIVE_RUN_PATH=/params/ready

#echo "moving run file to spartan"
#local_run_path="params/ready/t_step0.010000__time_T10__instance_index1.000000__n_qubits4.000000__graph_typeSparse.yml"
#local_run_path="_main_.py"
#scp $local_run_path $HOST_NAME:$CLUSTER_URI$RELATIVE_RUN_PATH
#scp $local_run_path $HOST_NAME:$CLUSTER_URI

dir=params/ready
for f in $dir/*
do
  local_run_path=$f
  echo $local_run_path
  scp $local_run_path $HOST_NAME:$CLUSTER_URI$RELATIVE_RUN_PATH
done
