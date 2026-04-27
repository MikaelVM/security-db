## Project Challenges and Potential Future Work
This section documents the key technical challenges encountered during development.

### Psycopg3 - String Composition for SQL Queries
**Challenge:** Safely composing SQL queries that include dynamic identifiers (e.g., usernames) while preventing SQL 
injection.

During development, I wanted a flexible way to construct SQL queries with dynamic values. While standard parameter 
substitution works well for values, it cannot be used for SQL identifiers such as table or column names. To address 
this, Psycopg3 requires the use of the Identifier class from the psycopg.sql module when inserting identifiers into 
queries.

Although this approach improves security by preventing SQL injection, it proved to be cumbersome in practice. 
The syntax is relatively verbose, and the available documentation and community examples are limited, making it 
timeconsuming to implement correctly. 

Due to time constraints and the added complexity, this feature was not implemented.

### PostgreSQL Role Management
**Challenge:** PostgreSQL's role and privilege system is complex and non-intuitive. The learning curve was steep, 
particularly with understanding:

- How to create and manage roles with proper hierarchies
- The difference between roles, users, and groups
- How privileges propagate (or don't propagate) through role memberships

Notably, roles assigned to a user does not automatically grant permissions to other user(s) if the role would do so by
itself.
For example, we have a role A that has permissions to create tables and then also assign reading privileges to user A 
for each table that it creates. If role A is assigned to user B, then when user B creates a new table, user A will not
automatically have permissions to read that table.

Instead, the user B must must also have assigned the paramaters to automatically assign read permissions, such that it
also grants read permissions to user A when user B creates a new table.

This adds a layer of complexity, as can be seen in [10_privileges.sql](sql/create_user/10_privileges.sql) and the
create_user folder in general.