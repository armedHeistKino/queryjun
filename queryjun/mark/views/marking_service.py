import time

from ..models import GuessResult, ResultType, GuessResultError
from ...submit.models import Guess
from ...member.models import Member

from .database_fetcher import DatabaseFetcher

class DefaultMarkingService:
    """
        A service layer for query marking
    """
    def __init__(self, member: Member, guess: Guess, db_fetcher: DatabaseFetcher):
        self.member: Member = member
        self.guess: Guess = guess
        self.db_fetcher: DatabaseFetcher = db_fetcher

    def _compare(self) -> bool | Exception:
        """
            Compare result from query guess and question answer
            Return True if same 
        """
        try:
            guess_result = self.db_fetcher.fetch_query_result(self.guess)
        except Exception as e:
            raise e
        
        answer = self.guess.question.answer
        return str(guess_result) == answer

    def _execute_guess(self) -> tuple[bool, float] | Exception:
        """
            Get the result of comparison & measure query execution time
        """
        execute_stamp = time.time()
        try:
            is_match = self._compare()
        except Exception as e:
            raise e
        complete_stamp = time.time()

        return is_match, (complete_stamp - execute_stamp) * 1000
    
    def _decide_result(self, is_match: bool, execute_time, is_exception_raised: bool=False) -> ResultType:
        """
            Decide which result type should be the guess's mark result
        """
        execute_limit = self.guess.question.execution_limit_milisecond

        if is_exception_raised: # guess could not be exeucted
            return ResultType.objects.get(result_acronym='ERR')
        elif not is_match: # guess did not yield desired result
            return ResultType.objects.get(result_acronym='FL')
        elif execute_time > execute_limit: # guess execution surpassed the limit
            return ResultType.objects.get(result_acronym='OVT')
        else: # clear
            return ResultType.objects.get(result_acronym='CLR')

    def mark(self) -> GuessResult | Exception:
        """
            Mark query guess
        """
        exception_flag = False

        try:
            is_match, execute_time = self._execute_guess()
        except Exception as e:
            exception_flag = True
            exception_message = e

            is_match, execute_time = False, 0.0
            is_exception_raised = True
        else:
            is_exception_raised = False

        result = self._decide_result(is_match, execute_time, is_exception_raised)

        guess_result = GuessResult(
            total_execution_time=execute_time,
            result=result,
            guess=self.guess,
        )
        guess_result.save()

        if exception_flag:
            GuessResultError(
                exception_message=exception_message,
                guess_result=guess_result
            ).save()

        if result == ResultType.objects.get(result_acronym='CLR'):
            self.member.solved_question.add(self.guess.question)