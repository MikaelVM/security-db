from db_handler import DatabaseHandler
from pathlib import Path
from enum import Enum

class DBRole(Enum):
    """Enumeration for roles in the database."""
    READ_ONLY = 'pg_read_all_data'
    PIPELINE_MAINTAINER = 'pg_write_all_data'
    ANALYST = 'analyst'
    API_ACCESS_ORDER = 'read_public_order'
    API_ACCESS_REPORTS = 'read_reports'


def create_user(db_handler: DatabaseHandler, *, username: str, password: str, role: DBRole) -> None:
    """Creates a new user in the database with the specified username, password, and role.

    Args:
        db_handler (DatabaseHandler): An instance of the DatabaseHandler class to interact with the database.
        username (str): The username for the new user.
        password (str): The password for the new user.
        role (str): The role to be assigned to the new user (e.g., 'admin', 'read_only', 'pipeline_manager').
    """

    db_handler.run_query(f"SELECT 1 FROM pg_roles WHERE rolname='{username}';")
    create_user_query = f"""
    CREATE USER {username} WITH PASSWORD '{password}';
    GRANT {role.value} TO {username};
    """

    print(f"Creating user '{username}' with role '{role.value}'...")
    db_handler.run_query(create_user_query)


if __name__ == "__main__":
    db_config_file = Path('./configs/local_db_config.ini')
    db_handler = DatabaseHandler(db_config_file)

    # Init the database
    sql_folder = Path('./sql/init')
    for sql_file in sql_folder.glob('*.sql'):
        db_handler.run_query(sql_file.read_text())

    # Create users with different roles

    db_handler.run_query(f"CREATE USER administrator SUPERUSER PASSWORD 'admin_password';")

    create_user(db_handler, username='analyst', password='1234', role=DBRole.ANALYST)

    # TODO: Create a new config file for the analyst user and prove he can make a new table with data in their own schema.

    create_user(db_handler, username='MikaelVM', password='ProperPassword@42', role=DBRole.PIPELINE_MAINTAINER)

    #create_user(db_handler, username='website_order_access', password='secret', role=DBRole.API_ACCESS_ORDER)

    #create_user(db_handler, username='report_access', password='secret', role=DBRole.API_ACCESS_REPORTS)

    # TODO: Create config file for report_access user and test that it can only read from the tables in the reports schema and not from the public schema.


