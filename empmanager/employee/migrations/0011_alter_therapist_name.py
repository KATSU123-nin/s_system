# Generated by Django 4.1.7 on 2023-03-05 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0010_alter_therapist_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="therapist",
            name="name",
            field=models.CharField(max_length=20, verbose_name="セラピスト名"),
        ),
    ]
