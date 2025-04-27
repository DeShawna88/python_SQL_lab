drop table if exists companies;
drop table if exists employees;

create table companies (
  id serial primary key,
  name varchar(255),
  industry varchar(100),
  headquarters varchar(255),
  founded_date date,
  website varchar(255)
);

CREATE TABLE employees (
  id serial primary key,
  company_id INTEGER NOT NULL
             REFERENCES companies(id)
             ON DELETE CASCADE,
  first_name varchar(100) NOT NULL,
  last_name varchar(100) NOT NULL,
  email varchar(255) NOT NULL UNIQUE,
  job_title varchar(100),
  hire_date date,
  salary numeric(12,2),
  is_active boolean NOT NULL DEFAULT TRUE
);
-- (Optional) index to speed up lookups by last name
CREATE INDEX idx_employees_last_name ON employees(last_name);