from django.apps import AppConfig


class MembershipsConfig(AppConfig):
    name = 'memberships'

    def ready(self):
        import users.signals
