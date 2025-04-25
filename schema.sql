DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS companies;

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    industry VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
);