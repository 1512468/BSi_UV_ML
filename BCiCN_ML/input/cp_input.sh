#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');

cp /root/docker-airflow/plugins/ML/input/BCiCN_$yesterday.csv /root/git_ml/input;

echo done
