#!/bin/bash

(bash ./data_collector/start_server.sh) &
(sleep 5 ; bash ./data_collector/download_data.sh)

python3 ./data_collector/unzip_file.py
