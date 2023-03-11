from django.apps import AppConfig
from .Modules import get_excel_data


class PatientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "patient"

    def ready(self):
        # 最初の1回だけ実行される関数
        get_excel_data
        print("Hello, World!")
