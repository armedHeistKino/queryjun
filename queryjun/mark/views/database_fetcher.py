import psycopg
from time import time as clock

from ...submit.models import Guess

from .database_configuration import POSTGRESQL_HOST, POSTGRESQL_DB_NAME , POSTGRESQL_USERNAME, POSTGRESQL_PASSWORD, POSTGRESQL_PORT

class DatabaseFetcher:
    """
        An interface for Database access
    """
    def __init__(self, guess: Guess):
        """

        """
        raise Exception("Method must be implemented")
    
    def execute_guess(self) -> list[tuple]:
        """
            Execute the given query & fetch result from database
            :param guess: source of guessed query
        """
        raise Exception("Method must be implemented")

    def time(self) -> None | float: 
        """
            Return a query execution time
        """
        raise Exception("Method must be implemented")
    
    def result(self) -> None | list[tuple[str | float | int]]:
        """
            Return a fetched result after executing a query
        """
        raise Exception("Method must be implemented")
    
    def is_query_overtime(self) -> bool:
        """
            True if query executing time has surpassed its limit
        """
        raise Exception("Method must be implemented")
    
    def has_query_exception(self) -> bool:
        """
            True if query have problem executed in DBMS
        """
        raise Exception("Method must be implemented")
    
    def query_exception(self) -> str:
        """
            Get query exception hints
        """
        raise Exception("Method must be implemented")

class PostgresqlFetcher(DatabaseFetcher):
    """
        Service layer for executing queries & fetch result in a PostgreSQL database 
    """
    def __init__(self, guess: Guess):
        """
            :param guess: 
        """
        self.connection = psycopg.connect(
            host=POSTGRESQL_HOST, 
            dbname=POSTGRESQL_DB_NAME, 
            user=POSTGRESQL_USERNAME, 
            password=POSTGRESQL_PASSWORD,
            port=POSTGRESQL_PORT,
        )
        self.cursor = self.connection.cursor()
        self.guess = guess

        self.is_exception_raised = False

    def execute_guess(self) -> None:
        """
            Execute a query and fetch result in a PostgreSQL database
        """
        try:
            start_stamp = clock()
            self.cursor.execute(self.guess.query_guessed)
            self.fetch_result = self.cursor.fetchall()
            end_stamp = clock()
        except Exception as e:
            self.fetch_time = (clock() - start_stamp) * 1000
            self.is_exception_raised = True
            self.exception = e
        else:
            self.fetch_time = (end_stamp - start_stamp) * 1000
        
    def time(self) -> None | float:
        """
            Return total time from executing a given query, to fetching a following reulst
                - internally call the tiem as fetch_time
        """
        return self.fetch_time
    
    def result(self) -> None | list[tuple]:
        return self.fetch_result
    
    def has_query_exception(self): 
        return self.is_exception_raised
    
    def query_exception(self): 
        return str(self.exception)
    
    def is_query_overtime(self):
        """
            Temporal constant
        """
        return self.fetch_time > self.guess.question.execution_limit_milisecond