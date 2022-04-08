#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project='BCi'
cp /root/airflow/plugins/ml/input/BCi_$yesterday.csv /root/git_ml/$project/input;
echo done
