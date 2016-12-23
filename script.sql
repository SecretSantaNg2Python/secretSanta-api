
drop database secretsanta;


CREATE DATABASE secretsanta
  WITH OWNER = postgres
       ENCODING = 'UTF8'
       TABLESPACE = pg_default
       LC_COLLATE = 'en_US.UTF-8'
       LC_CTYPE = 'en_US.UTF-8'
       CONNECTION LIMIT = -1;

CREATE EXTENSION "uuid-ossp";


	drop table
	  if exists users,

	 cascade;


/* CREATE TABLEs */

CREATE TABLE users (
id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
account_id UUID references accounts(id),
full_name varchar(50) not null,
email varchar(50) unique not null,
password TEXT not null,
active boolean default true,
modified_by varchar(255) default 'postgresql',
last_modified timestamp DEFAULT current_timestamp,
created timestamp DEFAULT current_timestamp
);