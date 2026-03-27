CREATE USER northwind_admin WITH LOGIN PASSWORD 'admin';

GRANT ALL PRIVILEGES ON DATABASE northwind_with_security TO northwind_admin; -- Does not pertain to objects in the DB
GRANT reports_owner to northwind_admin;
GRANT public_owner to northwind_admin;
