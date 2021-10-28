#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');

cp /root/git_ml/output/ML_$yesterday.csv /root/docker-airflow/plugins/ML/output

echo done
