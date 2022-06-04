# OOD project

Spring 1401

Team 1

## Members

Mohsen Dehghankar

Sajjad Reyhani

Seyyed Mahdi Faghih

Sepehr Safari

## Getting Started
### Install
```
python -m venv ./venv
python -m pip install -r requirements.txt
source ./venv/bin/activate
```

### Run in Container
Follow these steps:
```
make build_docker
make run_docker
```

### Run Local
Follow these steps:
```
make start_db
make migrate
make run
```

### Finish
```
make stop
```
