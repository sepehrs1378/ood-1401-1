from services.controller.controller import ServiceController
from services.view.views import ServiceView
from users.controller.controller import UserController
from users.view.views import UserView


class DependencyInjector:
    def __init__(self) -> None:
        # Controllers
        self.user_controller = UserController()
        self.service_controller = ServiceController()

        # Views
        self.user_view = UserView(self.user_controller)
        self.service_view = ServiceView(self.service_controller)


dependency_injector = DependencyInjector()
