DROP TABLE IF EXISTS phonebook;

CREATE TABLE phonebook(
  id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  phone_number BigInt 
)