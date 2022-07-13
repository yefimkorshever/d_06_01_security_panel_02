# Bank checkpoint

The program renders bank checkpoint website using Django ORM

## Prerequisites

Python 3.10 or higher required.

## Installing

- Download the project files
- Set up packages:

```bash
pip install -r requirements.txt
```

- Set up environmental variables in your operating system or in .env file. The variables are:
  - `BANK_BASE_HOST` (obligatory)
  - `BANK_BASE_NAME` (obligatory)
  - `BANK_BASE_USER` (obligatory)
  - `BANK_BASE_PASSWORD` (obligatory)
  - `CHECKPOINT_SECRET_KEY` (obligatory)
  - `CHECKPOINT_DEBUG` (optional, False by default)
  - `CHECKPOINT_ALLOWED_HOSTS` (obligatory when CHECKPOINT_DEBUG is False)

To set up variables in .env file, create it in the root directory of the project and fill it up like this:

```bash
BANK_BASE_HOST=bank.example.org
BANK_BASE_NAME=example_base
BANK_BASE_USER=example_name
BANK_BASE_PASSWORD=example_pass
CHECKPOINT_SECRET_KEY=example_key
CHECKPOINT_DEBUG=False
CHECKPOINT_ALLOWED_HOSTS=localhost,127.0.0.1,mywebsite.example
```

## Running script

- Run:

```bash
python manage.py runserver 0.0.0.0:8000
```

- Go to [Bank checkpoint website](http://127.0.0.1:8000/)

## Project goals

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org)
