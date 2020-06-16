#!/bin/bash

set -e
run_file="params/ready/t_step0.010000__time_T10__instance_index1.000000__n_qubits4.000000__graph_typeSparse.yml"

dir=params/ready
for f in $dir/*
do
  local_run_path=$f
  echo $local_run_path
done
#sbatch --mem 10GB --output=tests.log bin/run-experiments.slurm $run_file
