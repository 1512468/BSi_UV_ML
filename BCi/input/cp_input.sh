#!/bin/bash
yesterday=$(date -d '- 1 day' '+%Y-%m-%d');
project=('BCi')
s= /root/docker-airflow/plugins/ML/input/BCi_$yesterday.csv /root/git_ml/$project/input;
echo $s
echo done
