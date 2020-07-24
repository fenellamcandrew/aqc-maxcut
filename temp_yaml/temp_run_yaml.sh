#!/bin/bash

dir=temp_yaml/yaml
for f in $dir/*
do
  local_run_path=$f
  echo $local_run_path
  python3 _main_.py --run_path="$local_run_path"
done
