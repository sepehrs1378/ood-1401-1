from .user import User


class ITManager(User):
    """
    This class represents an ITManager user
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.is_superuser = True
        self.is_staff = True

    class Meta:
        verbose_name = "ITManager"
        verbose_name_plural = "ITManagers"
