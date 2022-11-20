from peewee import *

db = PostgresqlDatabase('phonebook', user='', password='',
                        host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class phonebook(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = BigIntegerField()

db.connect()

def app_logic():
  print('Welcome to contacts in your phonebook!')
  answer = input('Select (C) to view your contacts or (A) to add a new contact or (F) to find a contact by first name' ).lower()

  if answer == 'a':
    first_name = input("Please enter contacts first name: " )
    last_name = input("Please enter contacts last name: " )
    phone_number = input("Please enter contacts phone number: " )
    
    contact = phonebook(first_name = first_name, last_name = last_name, phone_number = phone_number)
    contact.save() 
    print(f"Contact {first_name} {last_name} has been saved under {phone_number}")
  elif answer == 'c':
    all_contacts = phonebook.select()
    for contact in all_contacts:
      print(f"{contact.first_name} {contact.last_name} {contact.phone_number}")
  elif answer == 'f':
    name = input('Please enter the first name you would like to search by: ').lower()
    all_contacts = phonebook.select()
    for contact in all_contacts:
      if name == contact.first_name.lower():
        print(f"{contact.first_name} {contact.last_name} {contact.phone_number}")
  app_logic()



app_logic()