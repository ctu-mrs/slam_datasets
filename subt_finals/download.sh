#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

## #{ download_data()
download_data() {
  URL=$1
  DOWNLOAD_FILE=$2
  if wget --no-check-certificate --content-disposition "${URL}" -O "${DOWNLOAD_FILE}"; then
    echo "wget of data was successfull"
  else
    echo "wget of data was unsuccessfull"
    echo " url: $URL"
    echo " download file: $DOWNLOAD_FILE"
  fi
} 
## #}

######################################################
# Add datasets here:
echo Downloading data for dataset: DARPA Subterranean Challenge, Finals

URL=( "." "https://nasmrs.felk.cvut.cz/index.php/s/mf0K9r8rmBcAiav/download" # maps
      "uav21_2" "https://nasmrs.felk.cvut.cz/index.php/s/GNP4S6FWdj2FuSC/download"
      "uav21_3" "https://nasmrs.felk.cvut.cz/index.php/s/bR5O4Z71QNeOsks/download"
      "uav21_4" "https://nasmrs.felk.cvut.cz/index.php/s/WNAnezo38I99zpH/download"
      "uav21_5" "https://nasmrs.felk.cvut.cz/index.php/s/4W7o12Uxb6VQwpy/download"
      "uav21_6" "https://nasmrs.felk.cvut.cz/index.php/s/vRzfLKcNueDxAoH/download"
      "uav22_1" "https://nasmrs.felk.cvut.cz/index.php/s/RaFXsset6szhWeR/download"
      "uav22_2" "https://nasmrs.felk.cvut.cz/index.php/s/WEaEOFzQZcJN2vj/download"
      "uav22_3" "https://nasmrs.felk.cvut.cz/index.php/s/LwfoPJ2gvCLqYpd/download"
      "uav24_1" "https://nasmrs.felk.cvut.cz/index.php/s/Rbzuz6oFk6Vpwds/download" )

######################################################

# Do not change below!
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
for (( i=0; i<${#URL[@]}; i+=2 ));
do
  DATASET="${URL[$i]}"
  TMP_FILE="/tmp/${DATASET}.tar.gz"

  echo -e "Processing data for: ${GREEN}${DATASET}${NC}"

  # download
  download_data "${URL[$i+1]}" "${TMP_FILE}"

  # untar
  tar -xvf "${TMP_FILE}" -C "${SCRIPT_PATH}/${DATASET}"
  rm "${TMP_FILE}"

  # rename to rosbag.bag
  if [ -f "${SCRIPT_PATH}/${DATASET}/${DATASET}.bag" ]; then
    mv "${SCRIPT_PATH}/${DATASET}/${DATASET}.bag" "${SCRIPT_PATH}/${DATASET}/rosbag.bag"
  fi

done
