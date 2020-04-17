#!/usr/bin/env bash

if [[ $1 == "small" ]]; then
    # download iot_23_datasets_small.tar.gz
    [[ ! -f iot_23_datasets_small.tar.gz ]] && \
    echo "[+] start download iot_23_datasets_small.tar.gz" && \
    wget --no-check-certificate https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/iot_23_datasets_small.tar.gz
    # tar -xvzf iot_23_datasets_small.tar.gz
    tar -xvzf iot_23_datasets_small.tar.gz opt/Malware-Project/BigDataset/IoTScenarios/CTU-IoT-Malware-Capture-17-1/bro/conn.log.labeled
elif [[ $1 == "full" ]]; then
    echo "TODO"
    exit 1
    # download iot_23_datasets_small.tar.gz
    [[ ! -f https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/iot_23_datasets_full.tar.gz ]] && \
        echo "[+] start download iot_23_datasets_full.tar.gz" && \
    wget --no-check-certificate https://mcfp.felk.cvut.cz/publicDatasets/IoT-23-Dataset/iot_23_datasets_full.tar.gz
    tar -xvzf iot_23_datasets_full.tar.gz
else
    echo "[*] Please select (full/small) dataset"
fi
