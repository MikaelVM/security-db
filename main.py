from configparser import ConfigParser

from db_handler import DatabaseHandler
from pathlib import Path
from enum import Enum
from configparser import ConfigParser
from rich import print

class DBRole(Enum):
    """Enumeration for roles in the database."""
    PG_READ = 'pg_read_all_data'
    PUBLIC_OWNER = 'public_owner'
    PUBLIC_READ = 'public_read'
    PUBLIC_WRITE = 'public_write'
    PUBLIC_READ_ORDER = 'public_read_order'
    REPORTS_OWNER = 'reports_owner'
    REPORTS_READ = 'reports_read'

class DBJob(Enum):
    """Enumeration for job roles, which are associated with one or more database roles."""
    DATA_INSPECTOR = [DBRole.PG_READ]
    DATA_ENGINEER = [DBRole.PUBLIC_READ, DBRole.PUBLIC_WRITE]
    ANALYST = [DBRole.REPORTS_OWNER]
    REPORT_VIEWER = [DBRole.REPORTS_READ]


def create_user(db_handler: DatabaseHandler, *, username: str, password: str, job: DBJob) -> None:
    """Creates a new user in the database with the specified username, password, and role.

    Args:
        db_handler (DatabaseHandler): An instance of the DatabaseHandler class to interact with the database.
        username (str): The username for the new user.
        password (str): The password for the new user.
        job (DBJob): The job role for the new user, which determines the database roles that will be granted to the user.
    """
    query = f"CREATE USER {username} WITH PASSWORD '{password}';"
    print(query)
    db_handler.run_query(f"CREATE USER {username} WITH PASSWORD '{password}';")

    for db_role in job.value:
        db_handler.run_query(f"GRANT {db_role.value} TO {username};")


if __name__ == "__main__":
    db_config_file = Path('configs/local_db_config.ini')
    db_config = ConfigParser()
    db_config.read(db_config_file)

    # Connect to admin_db to create the northwind_with_security database
    db_config['DBCONFIG']['dbname'] = 'postgres'
    db_handler = DatabaseHandler(db_config)

    # Drop and create the database to ensure a clean slate for the exercise.
    db_handler.run_query(Path('./sql/restart_nws_db.sql').read_text())
    db_handler.run_query("DROP DATABASE IF EXISTS northwind_with_security;")
    db_handler.run_query("CREATE DATABASE northwind_with_security;")

    # Connect to the newly created northwind_with_security database to initialize it.
    db_config['DBCONFIG']['dbname'] = 'northwind_with_security'
    db_handler = DatabaseHandler(db_config)

    # Init the database
    sql_folder = Path('./sql/init')
    for sql_file in sql_folder.glob('*.sql'):
        db_handler.run_query(sql_file.read_text())

    # Create users with different roles
    print(f"Creating user 'administrator' with SUPERUSER role...")
    db_handler.run_query(f"CREATE USER administrator SUPERUSER PASSWORD 'secret';")

    # create_user(db_handler, username='mikaelvm', password='secret', job=DBJob.DATA_ENGINEER)
    create_user(db_handler, username='jamessaunders', password='secret', job=DBJob.ANALYST)
    create_user(db_handler, username='reportsread', password='secret', job=DBJob.REPORT_VIEWER)

    # Connect to the database as the analyst user
    db_config['DBCONFIG']['user'] = 'jamessaunders'
    db_config['DBCONFIG']['password'] = 'secret'
    db_handler = DatabaseHandler(db_config)

    analyst_query = Path('./sql/analyst_query.sql').read_text()
    db_handler.run_query(analyst_query)

    print(len(db_handler.fetch_query_results("SELECT * FROM reports.sales_summary_month;")))

    db_config['DBCONFIG']['user'] = 'reportsread'
    db_config['DBCONFIG']['password'] = 'secret'
    db_handler = DatabaseHandler(db_config)

    # Should succeed as user 'reportsread' has read_reports role
    print(len(db_handler.fetch_query_results("SELECT * FROM reports.sales_summary_month;")))
    # Should fail due to lack of permissions
    print(len(db_handler.fetch_query_results("SELECT * FROM public.orders;")))

    # print list of users in the database

    print(db_handler.fetch_query_results(Path('./sql/select_users.sql').read_text()))


