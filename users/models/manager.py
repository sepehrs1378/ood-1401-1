from users.models.role import Role


class Manager(Role):
    """
    This class represents a Manager of the system
    """

    class Meta:
        verbose_name = "Manager"
        verbose_name_plural = "Managers"
