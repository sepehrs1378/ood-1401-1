from .user import User


class Expert(User):
    """
    An Expert is a User who provides services
    """

    class Meta:
        verbose_name = "Expert"
        verbose_name_plural = "Experts"
