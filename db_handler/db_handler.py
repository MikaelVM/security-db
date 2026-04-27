"""Module for running SQL queries on a PostgreSQL database."""
from configparser import ConfigParser
from pathlib import Path
from typing import Any

from psycopg import Connection, connect
from psycopg.sql import SQL


class DatabaseHandler:
    """A class for running SQL queries on a PostgreSQL database.

    Attributes:
        verbose (bool): Whether to print the SQL queries being executed and connection status messages for
        debugging purposes.
        connection_string (str): The connection string used to connect to the PostgreSQL database.
    """

    def __init__(self, config_file_path: Path | ConfigParser, *, verbose: bool = False) -> None:
        """Initialize the DatabaseHandler instance.

        Args:
            config_file_path (Path | ConfigParser): The path to the configuration file or a Config
            Parser object containing the database connection parameters.
            verbose (bool, optional): Whether to print the SQL queries being executed and connection status messages
            for debugging purposes. Defaults to False.
        """
        self.verbose = verbose
        self.connection_string = self._get_connection_string_from_config(config_file_path)

    def fetch_query_results(self, query: SQL | str, values: list[Any] = None) -> list[tuple]:
        """Execute a SQL query and fetch the results from the PostgreSQL database.

        Args:
            query (SQL | str): The SQL query to be executed, either as a psycopg SQL object or a regular string.
            values (list[Any], optional): A list of values to be passed to the query. Defaults to None.
        """
        connection = self._get_postgres_connection()
        try:
            if isinstance(query, str):
                query = SQL(query)

            print("Running query: \n" + '-' * 50 + f"\n{query.as_string(connection)}\n") if self.verbose else None
            print('-' * 50) if self.verbose else None

            with connection as conn:

                if values:
                    result = conn.execute(query, values)
                else:
                    result = conn.execute(query)

                return result.fetchall()

        except Exception as e:
            print(f"Error executing query: {e}")
            return []

    def run_query(
            self,
            query: SQL | str, values: tuple[Any] | dict[str, Any] = None,
            raise_error: bool = True,
            autocommit: bool = False
    ) -> bool:
        """Execute a SQL query on the PostgreSQL database.

        Args:
            query (SQL | str): The SQL query to be executed, either as a psycopg SQL object or a regular string.
            values (tuple[Any] | dict[str, Any], optional): A tuple or dictionary of values to be passed to the query.
                Defaults to None.
            raise_error (bool, optional): Whether to raise an exception if the query execution fails. Defaults to False.
            autocommit (bool, optional): Whether to enable autocommit mode for the connection. Defaults to False.

        Raises:
            Exception: If the query execution fails and raise_error is set to True.
        """
        connection = self._get_postgres_connection()
        try:
            if isinstance(query, str):
                query = SQL(query)

            print("Running query: \n" + '-' * 50 + f"\n{query.as_string(connection)}\n") if self.verbose else None
            print('-' * 50) if self.verbose else None

            with connection as conn:
                if autocommit:
                    conn.autocommit = True
                if values:
                    conn.execute(query, values)
                else:
                    conn.execute(query)
            return True

        except Exception as e:
            if raise_error:
                raise Exception(f"Error executing query: {e}")
            return False

    def _get_postgres_connection(self) -> Connection:
        """Establish a connection to the PostgreSQL database using the connection string.

        Raises:
            Exception: If there is an error connecting to the PostgreSQL database.
        """
        try:
            connection = connect(self.connection_string)
            print("Connection to PostgreSQL database established successfully.") if self.verbose else None
            return connection

        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            raise

    @staticmethod
    def _get_connection_string_from_config(config_file_path: Path | ConfigParser) -> str:
        """Read database connection parameters from a configuration file and constructs a connection string.

        Args:
            config_file_path (Path | ConfigParser): The path to the configuration file or a ConfigParser object.
        """
        if isinstance(config_file_path, ConfigParser):
            config = config_file_path
        else:
            config = ConfigParser()
            config.read(config_file_path)

        host = config['DBCONFIG']['host']
        port = config['DBCONFIG']['port']
        dbname = config['DBCONFIG']['dbname']
        user = config['DBCONFIG']['user']
        password = config['DBCONFIG']['password']

        connection_string = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
        return connection_string
