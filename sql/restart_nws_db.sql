-- This script is used to restart the northwind_with_security database

-- Terminate all connections to the northwind_with_security database
SELECT pg_terminate_backend(pid)
FROM pg_stat_activity
WHERE datname = 'northwind_with_security'
AND leader_pid IS NULL;
