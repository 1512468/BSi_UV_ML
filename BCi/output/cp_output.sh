#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project='BCi'
cp /root/git_ml/$project/output/BCi_$yesterday.csv /root/airflow/plugins/ml/output

echo done
