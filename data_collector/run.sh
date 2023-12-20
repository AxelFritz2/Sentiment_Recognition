#!/bin/bash

(bash start_server.sh) & 
(sleep 5 ; bash download_data.sh)

python3 unzip_file.py
