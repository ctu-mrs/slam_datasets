#!/bin/bash

DEFAULT_DATASETS="bull_rock_cave,subt_finals"
ALLOWED_DATASETS=( "bull_rock_cave" "subt_finals" )

# Do not change below

if [ "$#" -eq 1 ]; then
  DATASETS="$1"
else
  DATASETS="$DEFAULT_DATASETS"
fi

for DATASET in "${ALLOWED_DATASETS[@]}"
do

  if [[ $DATASETS == *"$DATASET"* ]]; then
    ./"$DATASET"/download.sh
  fi

done
