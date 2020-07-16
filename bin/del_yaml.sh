#!/bin/bash

dir=params/ready
for f in $dir/*
do
  local_run_path=$f
  rm $local_run_path
done
