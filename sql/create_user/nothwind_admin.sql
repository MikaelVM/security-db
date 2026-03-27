CREATE USER northwind_admin WITH LOGIN PASSWORD 'admin';

 -- Does not grant privileges on schemas or tables, only on the database itself
GRANT ALL PRIVILEGES ON DATABASE northwind_with_security TO northwind_admin;

-- Grant privileges on existing tables and future tables in the public and reports schemas
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO northwind_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public FOR ROLE postgres GRANT ALL PRIVILEGES ON TABLES TO northwind_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA public FOR ROLE administrator GRANT ALL PRIVILEGES ON TABLES TO northwind_admin;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA reports TO northwind_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE postgres GRANT ALL PRIVILEGES ON TABLES TO northwind_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE administrator GRANT ALL PRIVILEGES ON TABLES TO northwind_admin;
ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE reports_owner GRANT ALL PRIVILEGES ON TABLES TO northwind_admin;