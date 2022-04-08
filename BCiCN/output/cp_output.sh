#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project='BCiCN'
cp /root/git_ml/$project/output/BCiCN_$yesterday.csv /root/airflow/plugins/ml/output

echo done
