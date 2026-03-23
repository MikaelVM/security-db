-- For development purposes and testing.

-- Drop all roles
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT rolname FROM pg_roles WHERE rolname NOT LIKE 'pg_%' AND NOT rolname = 'postgres') LOOP
        EXECUTE 'DROP OWNED BY ' || quote_ident(r.rolname);
        EXECUTE 'DROP ROLE IF EXISTS ' || quote_ident(r.rolname);
    END LOOP;
END $$;

-- Drop all tables
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;
