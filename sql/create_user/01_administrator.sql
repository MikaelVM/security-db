CREATE USER administrator SUPERUSER PASSWORD 'admin';

-- Quote from the Postgres documentation on superusers (21.2. Role Attributes):
--   A database superuser bypasses all permission checks, except the right to log in.
--   This is a dangerous privilege and should not be used carelessly.
--   It is best to do most of your work as a role that is not a superuser.

-- Notably does not have the ability to create their own databases.
