from src.models.repositories.users_repository import UsersRepository
from src.controllers.user_finder import UserFinder
from src.views.user_finder_view import UserFinderView

def user_finder_componser():
    model = UsersRepository()
    controller = UserFinder(model)
    view = UserFinderView(controller)
    return view 

