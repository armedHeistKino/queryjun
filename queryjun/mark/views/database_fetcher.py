import psycopg

from ...submit.models import Guess

from .database_configuration import POSTGRESQL_HOST, POSTGRESQL_DB_NAME , POSTGRESQL_USERNAME, POSTGRESQL_PASSWORD, POSTGRESQL_PORT

class DatabaseFetcher:
    """
        An interface for Database access
    """
    def fetch_query_result(self, guess: Guess) -> list[tuple]:
        """
            Execute the given query & fetch result from database
            :param guess: source of guessed query
        """
        return Exception("Method must be implemented")

class PostgresqlFetcher(DatabaseFetcher):
    """
        Service layer for executing queries & fetch result in a PostgreSQL database 
    """
    def __init__(self):
        self.connection = psycopg.connect(
            host=POSTGRESQL_HOST, 
            dbname=POSTGRESQL_DB_NAME, 
            user=POSTGRESQL_USERNAME, 
            password=POSTGRESQL_PASSWORD,
            port=POSTGRESQL_PORT,
        )
        self.cursor = self.connection.cursor()

    def fetch_query_result(self, guess: Guess) -> list[tuple]:
        """
            Execute and fetch in a PostgreSQL database
            :param guess:
        """
        try:
            self.cursor.execute(guess.query_guessed)
            result = self.cursor.fetchall()
        except Exception as e:
            raise e 
        return result