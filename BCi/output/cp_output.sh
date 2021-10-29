#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project=('BCi')
cp /root/git_ml/$project/output/BCi_$yesterday.csv /root/docker-airflow/plugins/ML/output

echo done
