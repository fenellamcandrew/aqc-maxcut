#!/bin/bash

set -e
run_file="params/ready/t_step0.010000__time_T10__instance_index1.000000__n_qubits4.000000__graph_typeSparse.yml"

dir=params/ready
for f in $dir/*
do
  local_run_path=$f
#  echo $local_run_path
  echo -e "Submitting job: \t $local_run_path"

  # Define run_file and log_file
  prefix="params/ready/"
  export log_file=logs/${local_run_path#"$prefix"}.log

  echo -e "Logging results: \t $log_file"

# Identify number of qubits
  N_QUBITS=$(echo $local_run_path | grep -oP '(?<=n_qubits)[0-9]+')

# Dynamically allocate memory based on N_QUBITS
  if (( $N_QUBITS >= 15 ))
  then
    # Allocate all RAM
    export NodeMemory=80GB
  elif (( N_QUBITS == 14 ))
  then
    export NodeMemory=40GB
  else
    export NodeMemory=10GB
  fi
  echo "Allocating node $NodeMemory memory for experiment $local_run_path"

  # Run experiment as an instance of the singularity container
  sbatch --mem $NodeMemory --output=$log_file bin/run-experiments.slurm $local_run_path
done
#sbatch --mem 10GB --output=tests.log bin/run-experiments.slurm $run_file
