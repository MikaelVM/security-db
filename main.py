from configparser import ConfigParser

from db_handler import DatabaseHandler
from pathlib import Path
from configparser import ConfigParser
from rich import print
from rich.console import Console

if __name__ == "__main__":
    db_config_file = Path('configs/local_db_config.ini')
    db_config = ConfigParser()
    db_config.read(db_config_file)
    db_handler = DatabaseHandler(db_config)
    console = Console()

    # Drop and create the database to ensure a clean slate for the exercise.
    console.log('Dropping and creating database northwind_with_security...', style='yellow')
    db_handler.run_query(Path('sql/terminate_connections.sql').read_text())
    db_handler.run_query("DROP DATABASE IF EXISTS northwind_with_security;")
    db_handler.run_query("CREATE DATABASE northwind_with_security;")
    console.log('Database northwind_with_security created successfully.', style='green')

    # Connect to the newly created northwind_with_security database to initialize it.
    console.log('Connecting to the newly created database northwind_with_security...', style='yellow')
    db_config['DBCONFIG']['dbname'] = 'northwind_with_security'
    db_handler = DatabaseHandler(db_config)
    console.log('Connected to database northwind_with_security successfully.', style='green')

    # Init the database
    console.log('Initializing the database with schema and data...', style='yellow')
    sql_folder = Path('./sql/init')
    for sql_file in sql_folder.glob('*.sql'):
        console.log('Running SQL file: ' + sql_file.name)
        db_handler.run_query(sql_file.read_text())
    console.log('Database initialized successfully.', style='green')

    # Create users with different roles
    console.log('Creating users with different roles...', style='yellow')
    sql_folder = Path('./sql/create_user')
    for sql_file in sql_folder.glob('*.sql'):
        console.log('Running SQL file: ' + sql_file.name)
        db_handler.run_query(sql_file.read_text())
    console.log('Users created successfully.', style='green')

    console.log('Fetching list of users in the database:', style='blue')
    console.print(
        db_handler.fetch_query_results(
            Path('./sql/select_users.sql').read_text()
        )
    )

    console.line()

    # Connect to the database as the analyst user
    console.log('Connecting to the database as the analyst user.', style='yellow')
    db_config['DBCONFIG']['user'] = 'grahamstark'
    db_config['DBCONFIG']['password'] = 'secret'
    db_handler = DatabaseHandler(db_config)
    console.log('Connected to the database as the analyst user successfully.', style='green')

    console.log('Creating sales summary report as the analyst user in the reports schema, '
                'from data in the public schema.', style='blue')
    analyst_query = Path('./sql/analyst_query.sql').read_text()
    db_handler.run_query(analyst_query)
    console.log('Showing first row from the new table created by the analyst user:', style='blue')
    console.print(db_handler.fetch_query_results("SELECT * FROM reports.sales_summary_month;")[0])

    console.line()

    # Connect to the database as the reports reader user
    console.log('Connecting to the database as the reports reader user.', style='yellow')
    db_config['DBCONFIG']['user'] = 'reports_api'
    db_config['DBCONFIG']['password'] = 'secret'
    db_handler = DatabaseHandler(db_config)
    console.log('Connected to the database as the reports reader user successfully.', style='green')

    if db_handler.run_query("SELECT * FROM reports.sales_summary_month;"):
        console.log('Successfully queried the sales summary report as the reports reader user.', style='green')
        console.log('Showing first row from the sales summary report as the reports reader user:', style='blue')
        console.print(db_handler.fetch_query_results("SELECT * FROM reports.sales_summary_month;")[0])
    else:
        console.log('Failed to query the sales summary report as the reports reader user.', style='red')

    if db_handler.run_query("SELECT * FROM public.orders;", raise_error=False):
        console.log('Successfully queried the orders table as the reports reader user.', style='green')
    else:
        console.log('Failed to query the orders table as the reports reader user due to lack of permissions.', style='red')
        console.log('This is expected behavior as the reports reader user should not have access to the orders '
                    'table, as it is in the public schema', style='purple')




