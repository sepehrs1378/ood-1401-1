# OOD project

Spring 1401\
Team 1

## Members

Mohsen Dehghankar\
Sajjad Reyhani\
Seyyed Mahdi Faghih\
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
/admin --> admin page
/users/register/expert --> register an expert user
/users/register/customer --> register a customer user
/users/login --> login
/services/request --> request a new service by customer
/services/approve/request_id --> approve a request by expert
/services/finish/request_id --> finish a request by expert
/messagin/ticket/create --> create a new ticket
/messaging/ticket/send --> send a new message to ticket
/messaging/ticket/show --> show a ticket details
/users/profile/customer --> edit customer profile
/users/profile/expert --> edit expert profile
```

## Sub-systems (= django apps)
- Users
- Messaging
- Feedback
- Reporting
- Service
- Admin (django admin is used)
