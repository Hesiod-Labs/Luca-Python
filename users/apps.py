from django.apps import AppConfig


# Set up the signaling of the Users class
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals