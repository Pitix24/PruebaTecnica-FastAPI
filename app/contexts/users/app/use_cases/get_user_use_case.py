from ...domain.repo.user_repo import UserRepository
from ..queries.get_user_query import GetUserQuery

class GetUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, query: GetUserQuery):
        return self.user_repository.get_by_id(query.user_id)
