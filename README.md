
# Scrapper


Install
```sh
pip install virtualenv
which python
>>> /path/to/python
virtualenv --python=/path/to/python .venv
```

Activate Enviroment
```sh
source .venv/bin/activate
```

## Run
```sh
sudo docker-compose up
sudo docker-compose up --scale worker=5 # 5 workers
```


### Manually

Terminal 1. (BROCKER)
```sh
docker run  -p 6379:6379 redis # BROCKER
```

Terminal 2. (WORKER)
```
celery -A scrapper worker --loglevel=info
```

Terminal 3. (SUBMIT JOB)
```sh
python
>>> from scrapper import do_work
>>> do_work.delay(5)
<AsyncResult: c2c13c5b-dbec-43da-878e-83b6114ee944>
```
> It will appear the result in the worker log

