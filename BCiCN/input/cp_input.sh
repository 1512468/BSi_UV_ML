#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project='BCiCN'
cp /root/airflow/plugins/ml/input/BCiCN_$yesterday.csv /root/git_ml/$project/input;

echo done
