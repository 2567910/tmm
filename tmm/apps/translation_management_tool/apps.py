from django.apps import AppConfig


class TranslationManagementToolConfig(AppConfig):
    name = 'tmm.apps.translation_management_tool'

    def ready(self):
        import tmm.apps.translation_management_tool.signals
