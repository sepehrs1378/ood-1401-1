from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates an ITManager user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument("--username", help="ITManager's username")
        parser.add_argument("--email", help="ITManager's email")
        parser.add_argument("--password", help="ITManager's password")

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username=options["username"]).exists():
            User.objects.create_superuser(
                username=options["username"],
                email=options["email"],
                password=options["password"],
            )
