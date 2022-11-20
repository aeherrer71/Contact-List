# Phonebook app

- This is a python built contact list that uses an SQL database and Peewee.

## Install Necessary Dependencies

- Peewee, psycopg2-binary, and autopep8

## Running the app

- CREATE DATABASE phonebook
- Run the sql schema file: psql -d phonebook < schema.sql
- Seed the data: psql -d phonebook < seed.sql
- start your virtual environment (pipenv shell)
- run python3 on the app.py file


### Functionality

- Program allows the user to view all contacts.
- Program allows the user to find a contact by first name.
- Program allows the user to add a new contact.
