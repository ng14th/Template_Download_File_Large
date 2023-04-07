#!/bin/bash
# example: run_dev.sh dev will use dev.env file

base_dir=$(pwd)

run_command="celery -A celery_worker.worker worker --loglevel=info -E"

echo "$run_command"
eval $run_command