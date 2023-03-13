from django.apps import AppConfig


class PatientConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "patient"

    def ready(self):
        # 最初の1回だけ実行される関数
        print("Hello, World!")
