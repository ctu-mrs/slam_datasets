#!/bin/bash

## #{ download_data()
download_data() {
  URL=$1
  DESTINATION_FOLDER=$2
  if wget --no-check-certificate --content-disposition "${URL}" -c -P "${DESTINATION_FOLDER}"; then
    echo "wget of data was successfull"
  else
    echo "wget of data was unsuccessfull"
    echo " url: $URL"
    echo " destination: $DESTINATION_FOLDER"
  fi
} 
## #}

######################################################
# Add datasets here:
echo Downloading data for dataset: Bull Rock Cave system
URL_MAP=https://nasmrs.felk.cvut.cz/index.php/s/BMY0MfH5Qc7g3AK/download
URL_0_FRONT=https://nasmrs.felk.cvut.cz/index.php/s/2MkQCtAFbxiv8G8/download
URL_1_BACK=https://nasmrs.felk.cvut.cz/index.php/s/wA1XXV5igy7Ge4u/download

# URLs for files and their respective subdirectories
URL=( "$URL_MAP" "$URL_0_FRONT" "$URL_1_BACK")
DATA_FOLDERS=( "." "0_front" "1_back" )
######################################################

# Do not change below!
SCRIPT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
for (( j=0; j<${#URL[@]}; j++ ));
do
  download_data "${URL[$j]}" "$SCRIPT_PATH/${DATA_FOLDERS[$j]}"
done
