
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


Run
```sh
sudo docker-compose up
sudo docker-compose up --scale worker=5 # 5 workers
```