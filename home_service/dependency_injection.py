from messaging.controller.controller import MessagingController
from messaging.view.views import MessagingView
from services.controller.controller import ServiceController
from services.view.views import ServiceView
from users.controller.controller import UserController
from users.view.views import UserView


class DependencyInjector:
    def __init__(self) -> None:
        # Controllers
        self.user_controller = UserController()
        self.service_controller = ServiceController()
        self.messaging_controller = MessagingController()

        # Views
        self.user_view = UserView(self.user_controller)
        self.service_view = ServiceView(self.service_controller)
        self.messaging_view = MessagingView(self.messaging_controller)


dependency_injector = DependencyInjector()
