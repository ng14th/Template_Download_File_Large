cmd_run_worker='dramatiq -p 4 -t 4 app.dramatiq_worker.worker:broker_rqm'
eval $cmd_run_worker
