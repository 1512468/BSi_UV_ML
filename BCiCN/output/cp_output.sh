#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project=('BCiCN')
cp /root/git_ml/$project/output/BCiCN_$yesterday.csv /root/docker-airflow/plugins/ML/output

echo done
