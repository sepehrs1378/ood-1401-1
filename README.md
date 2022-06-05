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
make run-docker
```

### Run Local

Follow these steps:

```
make start-db
make migrate
make run
```

### Finish

```
make stop
```

### Also create an ITManager to login to admin

```
make create-superuser
then go to localhost:8000/admin
```

## Important end-points
```
/admin
/users/register/expert
/users/register/customer
/users/login
/services/request
/services/approve/request_id
/services/finish/request_id
/messagin/ticket/create
/messaging/ticket/send
/messaging/ticket/show
```
