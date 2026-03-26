CREATE USER grahamstark WITH PASSWORD 'secret';
GRANT reports_owner TO grahamstark;
GRANT public_read TO grahamstark;
-- Ensure that reports_read has SELECT privileges on future table created by grahamstark in the reports schema
ALTER DEFAULT PRIVILEGES IN SCHEMA reports FOR ROLE grahamstark GRANT SELECT ON TABLES TO reports_read;
