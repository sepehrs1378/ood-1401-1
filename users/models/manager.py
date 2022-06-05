from .user import User


class Manager(User):
    """
    This class represents a Manager of the system
    """

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
