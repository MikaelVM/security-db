CREATE ROLE public_owner;
ALTER SCHEMA public OWNER TO public_owner;

CREATE ROLE public_read;
GRANT USAGE ON SCHEMA public TO public_read;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO public_read;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO public_read;

CREATE ROLE public_write;
GRANT USAGE ON SCHEMA public TO public_write;
GRANT INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO public_write;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT INSERT, UPDATE, DELETE ON TABLES TO public_write;

CREATE ROLE public_read_order;
GRANT USAGE ON SCHEMA public TO public_read_order;
GRANT SELECT ON orders TO public_read_order;

CREATE ROLE reports_owner;
CREATE SCHEMA reports AUTHORIZATION reports_owner;

CREATE ROLE reports_read;
GRANT USAGE ON SCHEMA reports TO reports_read;
GRANT SELECT ON ALL TABLES IN SCHEMA reports TO reports_read;
ALTER DEFAULT PRIVILEGES IN SCHEMA reports GRANT SELECT ON TABLES TO reports_read;
