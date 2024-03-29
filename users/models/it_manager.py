from users.models.role import Role


class ITManager(Role):
    """
    This class represents an ITManager user
    """

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.is_superuser = True
        self.is_staff = True

    def get_type_name(self):
        return "مدیر فنی"

    class Meta:
        verbose_name = "ITManager"
        verbose_name_plural = "ITManagers"

    def __str__(self):
        return "مدیر فنی"
