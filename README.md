# security-db
Exercises for trainig in security management of a database. 


# Issues encountered:

## Psycopg3:

### Proper [string composition](https://www.psycopg.org/psycopg3/docs/api/sql.html) for SQL queries to avoid SQL injection:

I wanted an easy way to compose SQL queries with variables, but since i needed to pass a variable into an identifier 
(username), I had to use the `Identifier` class from `psycopg3.sql` module, as psycopg3 does not allow parameter 
substitution for identifiers. This is a security measure to prevent SQL injection attacks.

However, this approach was very cumbersome, lacked in depth documentation and examples from other users. 
As I ran out of time, O could not implment the feature. 

## PostgreSQL:

### Role management:
PostgreSQL has a complex role management system, and I had to spend a lot of time understanding how to create roles, 
assign permissions, and manage access control.

I struggled with understanding 'ALTER DEFAULT PRIVILEGES ...' and how it works with schemas and tables. 
Mainly that roles assigned to a user do not automatically grant permissions to other user when they create new tables. 

I had to explicitly make stastement like 'ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE grahamstark GRANT SELECT 
ON TABLES TO reports_read;' to ensure that any new tables created in the 'reports' schema by 'grahamstark' would have 
SELECT permissions granted to the 'reports_read' role.



