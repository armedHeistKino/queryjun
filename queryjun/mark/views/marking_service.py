from ..models import GuessResult, ResultType, GuessResultError
from ...submit.models import Guess
from ...member.models import Member

from .database_fetcher import DatabaseFetcher
from .comparer import DefaultComparer

class DefaultMarkingService:
    """
        A service layer for query marking
    """
    def __init__(self, member: Member, guess: Guess, database_fetcher: DatabaseFetcher, comparer: DefaultComparer):
        """
        :param member:
        :param guess:
        :param database_fetcher:
        :param comparer:
        """
        self.member = member
        self.guess = guess
        self.database_fetcher = database_fetcher
        self.comparer = comparer

    def mark(self) -> None:
        """
            Practice total action of 'mark'
                - execute guessing query and fetch the result
                - decode result 
        """
        self.database_fetcher.execute_guess()
        
        result_type = self._decide_result_type()

        guess_result = GuessResult(
            total_execution_time = self.database_fetcher.time(),
            result=result_type,
            guess=self.guess
        )
        guess_result.save()
        
        if result_type == ResultType.objects.get(result_acronym='CLR'):
            self.member.solved_question.add(self.guess.question)

        if self.database_fetcher.has_query_exception():
            GuessResultError(
                exception_message=self.database_fetcher.query_exception(),
                guess_result=guess_result
            ).save()

    def _decide_result_type(self) -> ResultType:
        """
            Decide which result type should be the guess's mark result
        """
        rto = ResultType.objects

        if self.database_fetcher.has_query_exception():
            return rto.get(result_acronym='ERR')
        elif self.database_fetcher.is_query_overtime():
            return rto.get(result_acronym='OVTM')
        elif not self.comparer.is_match():
            return rto.get(result_acronym='FL')
        else:
            return rto.get(result_acronym='CLR')