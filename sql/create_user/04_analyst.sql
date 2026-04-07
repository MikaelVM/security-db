CREATE USER analyst WITH PASSWORD 'secret';
GRANT reports_owner TO analyst;
GRANT public_read TO analyst;
