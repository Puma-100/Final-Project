#!/bin/bash
mkdir data

input="./urls_for_data_download.txt"
while IFS= read -r line
do
  # Setting the base filename  
  filename=$(basename "$line")
  
  # Downloading the file  
  curl -o "$line" "$filename" 

  # Commenting the file has been download
  echo "Downloaded $filename" 
done < "$input"