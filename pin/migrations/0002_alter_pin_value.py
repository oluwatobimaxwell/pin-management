# Generated by Django 4.1.1 on 2022-11-02 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pin", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pin",
            name="value",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (100, "NGN 100"),
                    (200, "NGN 200"),
                    (300, "NGN 300"),
                    (400, "NGN 400"),
                    (500, "NGN 500"),
                ],
                default=100,
                null=True,
            ),
        ),
    ]
