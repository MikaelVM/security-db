CREATE USER analyst WITH PASSWORD 'secret';
GRANT reports_owner TO analyst;
GRANT public_read TO analyst;

-- Ensure that reports_read has SELECT privileges on future table created by others in the reports schema
ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE analyst GRANT SELECT ON TABLES TO reports_read;
