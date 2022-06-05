from .user import User


class Customer(User):
    """
    A Customer is a User who wants to get services
    """

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
