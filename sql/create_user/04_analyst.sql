CREATE USER analyst WITH PASSWORD 'secret';
GRANT reports_owner TO analyst;
GRANT public_read TO analyst;

-- Ensure that reports_read has SELECT privileges on future table created by others in the reports schema
