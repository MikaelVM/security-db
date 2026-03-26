"""Module for running SQL queries on a PostgreSQL database."""
from configparser import ConfigParser
from pathlib import Path
from typing import Any

from psycopg import Connection, connect
from psycopg.sql import SQL
from psycopg import sql

class DatabaseHandler:
    """A class for running SQL queries on a PostgreSQL database.

    Attributes:
        verbose (bool): Whether to print the SQL queries being executed and connection status messages.
        connection_string (str): The connection string used to connect to the PostgreSQL database.
    """

    def __init__(self, config_file_path: Path | ConfigParser, *, verbose: bool = False) -> None:
        self.verbose = verbose
        self.connection_string = self._get_connection_string_from_config(config_file_path)

    def fetch_query_results(self, query: SQL | str, values: list[Any] = None) -> list[tuple]:
        """Executes a SQL query and fetches the results from the PostgreSQL database.

        Args:
            query (SQL | str): The SQL query to be executed, either as a psycopg SQL object or a regular string.
            values (list[Any], optional): A list of values to be passed to the query. Defaults to None.
        """
        connection = self._get_postgres_connection()
        try:
            if isinstance(query, str):
                query = SQL(query)

            print(f"Running query: \n" + '-' * 50 +
                  f"\n{query.as_string(connection)}\n") if self.verbose else None
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

    def run_query(self, query: SQL | str, values: tuple[Any] | dict[str, Any] = None, raise_error: bool = True) -> bool:
        """Executes a SQL query on the PostgreSQL database.

        Args:
            query (SQL | str): The SQL query to be executed, either as a psycopg SQL object or a regular string.
            values (tuple[Any] | dict[str, Any], optional): A tuple or dictionary of values to be passed to the query. Defaults to None.
            raise_error (bool, optional): Whether to raise an exception if the query execution fails. Defaults to False.

        Returns:
            bool: True if the query was executed successfully, False otherwise.
        """
        connection = self._get_postgres_connection()
        try:
            if isinstance(query, str):
                query = SQL(query)

            print(f"Running query: \n" + '-' * 50 +
                  f"\n{query.as_string(connection)}\n") if self.verbose else None
            print('-' * 50) if self.verbose else None

            with connection as conn:
                conn.autocommit = True # NOTE: DON'T DO THIS IN PRODUCTION CODE! NOT PROPER TRANSACTION MANAGEMENT
                # I AM DOING THIS FOR SIMPLICITY IN THIS EXERCISE
                if values:
                    conn.execute(query, values)
                else:
                    conn.execute(query)

            return True
        except Exception as e:
            if raise_error:
                raise
            return False

    def bulk_insert(self, query: SQL, values: list[list[Any]]) -> bool:
        raise NotImplementedError("Bulk insert method is not implemented yet.")

    def _get_postgres_connection(self) -> Connection:
        """Establishes a connection to the PostgreSQL database using the connection string."""

        try:
            connection = connect(self.connection_string)
            print("Connection to PostgreSQL database established successfully.") if self.verbose else None
            return connection
        except Exception as e:
            print(f"Error connecting to PostgreSQL database: {e}")
            raise

    @staticmethod
    def _get_connection_string_from_config(config_file_path: Path | ConfigParser) -> str:
        """Reads database connection parameters from a configuration file and constructs a connection string.

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