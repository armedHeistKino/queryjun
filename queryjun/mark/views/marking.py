import time

from ...submit.models import Guess
from ...question.models import Question

from ..models import GuessResult
from ..models import ResultType

from .database_fetcher import DatabaseFetcher

class Marking:
    """
        A service layer for marking query guess

        240925 mark() -- too dirty! work again!
    """
    def __init__(self, guess: Guess, db_fetcher: DatabaseFetcher):
        self.guess: Guess = guess
        self.db_fetcher: DatabaseFetcher = db_fetcher

        self.question: Question = guess.question
        
    def _compare_answer(self) -> bool:
        """
            True if a guess makes a desired answer
        """
        result = self.db_fetcher.fetch_query_result(self.guess)
        return str(result) == self.question.answer
    
    def mark(self) -> GuessResult:
        """
            전체에 대한 채점
        """
        start = time.time()
        is_match_with_answer = self._compare_answer()
        end = time.time()
        
        execution_time = (end - start) * 1000
        
        if not is_match_with_answer:
            result_symbol = ResultType.objects.filter(result_acronym='FL').first()
        elif execution_time > self.question.execution_limit_milisecond:
            result_symbol = ResultType.objects.filter(result_acronym='OVT').first()
        else: 
            result_symbol = ResultType.objects.filter(result_acronym='CLR').first()
    
        guess_result = GuessResult(
            total_execution_time=execution_time,
            result=result_symbol,
            guess=self.guess,
        )
        guess_result.save()

        return guess_result
