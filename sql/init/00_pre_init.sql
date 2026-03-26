-- For development purposes and testing only.

-- Drop all roles except for the default ones (pg_*, postgres).
DO $$
DECLARE
    r RECORD;
BEGIN
    FOR r IN (SELECT rolname FROM pg_roles WHERE rolname NOT LIKE 'pg_%' AND NOT rolname = 'postgres') LOOP
        EXECUTE 'DROP OWNED BY ' || quote_ident(r.rolname);
        EXECUTE 'DROP ROLE IF EXISTS ' || quote_ident(r.rolname);
    END LOOP;
END $$;

